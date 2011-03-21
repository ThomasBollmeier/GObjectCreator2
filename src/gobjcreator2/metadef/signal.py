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


class Signal(object):

    def __init__(self,
                 name,
                 result,
                 result_modifiers
                 ):

        self.name = name
        self.internal_name = name.replace("-", "_")
        self.result = result
        self.result_modifiers = result_modifiers
        self.parameters = []

    def add_parameter(self, name, type, modifiers):

        self.parameters.append((name, type, modifiers))
