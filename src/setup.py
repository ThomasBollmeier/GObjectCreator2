#
# Copyright 2011 Thomas Bollmeier
#
# This file is part of GObjectCreator2.
#
# GObjectCreator2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GObjectCreator2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GObjectCreator2.  If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup

description = "Generation of source files in various languages"
description += " from meta definition files"

setup(
    name = "GObjectCreator2",
    version = "1.0.0",
    description = description,
    author = "Thomas Bollmeier",
    author_email = "TBollmeier@web.de",
    license = "GPLv3",
    packages = ["gobjcreator2", 
                "gobjcreator2/input",
                "gobjcreator2/metadef",
                "gobjcreator2/output"
                ],
    scripts = ["scripts/gobject_creator2.py"]
    )
