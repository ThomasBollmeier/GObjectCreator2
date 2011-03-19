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


from gobjcreator2.metadef.constants import \
    Visibility, Scope, MethodInheritance
from gobjcreator2.metadef.types import NULL

class Method(object):

    def __init__(self,
                 name,
                 result = NULL,
                 result_modifiers = [],
                 visibility = Visibility.PUBLIC,
                 scope = Scope.INSTANCE,
                 inheritance_mode = MethodInheritance.FINAL
                 ):

        self.name = name
        self.result = result
        self.result_modifiers = result_modifiers
        self.visibility = visibility
        self.scope = scope
        self.inheritance_mode = inheritance_mode
        self.parameters = []

    def add_parameter(self, param):

        self.parameters.append(param)

class InterfaceMethod(Method):

    def __init__(self,
                 name,
                 result = NULL,
                 result_modifiers = []
                 ):

        Method.__init__(self, name, result, result_modifiers,
                        Visibility.PUBLIC, Scope.INSTANCE,
                        MethodInheritance.ABSTRACT)