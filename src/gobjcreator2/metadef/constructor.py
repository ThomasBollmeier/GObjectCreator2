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


from gobjcreator2.metadef.method import Method, MethodInheritance
from gobjcreator2.metadef.constants import Scope, Visibility

class Constructor(Method):

    NAME = "new"

    def __init__(self,
                 cls,
                 ):

        Method.__init__(self,
                        Constructor.NAME,
                        result = cls,
                        result_modifiers = [],
                        visibility = Visibility.PUBLIC,
                        scope = Scope.STATIC,
                        inheritance_mode = MethodInheritance.FINAL
                        )

        self.property_inits = {}

    def init_property(self, name, value, is_code_value):

        self.property_inits[name] = (value, is_code_value)
