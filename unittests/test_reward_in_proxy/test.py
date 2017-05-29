#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

import unittest
import subprocess
import sys
import os


class RewardInProxyTest(unittest.TestCase):
    def test(self):
        if (sys.version_info[0] == 3):
            music_filename = "test_py3.music"
        else:
            music_filename = "test.music"
        subprocess.check_call(["mpirun", "-np", "2", "music", music_filename],
                              cwd=os.path.dirname(os.path.realpath(__file__)))


if __name__ == '__main__':
    unittest.main()
