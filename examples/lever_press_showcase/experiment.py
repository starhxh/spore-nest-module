#! /usr/bin/env python

#
# This file is part of SPORE.
#
# Copyright (C) 2016, the SPORE team (see AUTHORS).
#
# SPORE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# SPORE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SPORE.  If not, see <http://www.gnu.org/licenses/>.
#
# For more information see: https://github.com/IGITUGraz/spore-nest-module
#

import os
import sys
import subprocess


plotter = None
exitcode = -1

if "TEST_MODE" not in sys.argv[1:]:
    # don't create plotter in test mode
    try:
        dev0 = open("/dev/null", "w")
        plotter = subprocess.Popen([sys.executable, "./python/interface.py"], stdout=dev0)

    except:
        print("Error when running the plotter interface.")

try:
    os.chdir("python")

    if (sys.version_info[0] == 3):
        music_filename = "run_py3.music"
    else:
        music_filename = "run.music"

    print("Starting MUSIC/NEST simulation")

    cmd = ["mpirun", "-np", "3", "music", music_filename]
    cmd.extend(sys.argv[1:])

    exitcode = subprocess.call(cmd)

finally:
    if plotter is not None:
        plotter.kill()

sys.exit(exitcode)
