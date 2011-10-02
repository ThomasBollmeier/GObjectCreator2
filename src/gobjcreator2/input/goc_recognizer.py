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

from gobjcreator2.input.reader import Reader
from gobjcreator2.input.goc_visitor import VisitorStep1, VisitorStep2, VisitorStep3
from gobjcreator2.metadef.package import Package

class GOCRecognizer(object):

    def __init__(self):

        self._reader = Reader()

    def add_include_path(self, path):

        self._reader.addIncludePath(path)

    def process_file(self, file_name):

        self._reader.readFile(file_name)
       
        self._reader.walk(VisitorStep1())
        self._reader.walk(VisitorStep2())
        self._reader.walk(VisitorStep3())

        return Package.get_top()
