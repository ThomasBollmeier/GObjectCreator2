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


class MethodInfo(object):

    def __init__(self,
                method,
                defined_in
                ):

        self.method = method
        self.defined_in = defined_in

    def _abs_package_name(self):

        package = self.defined_in.package
        name = package.name
        while package.package:
            package = package.package
            if package.name:
                name = package.name + "::" + name

        return name

    def __str__(self):

        if self.defined_in.__class__.__name__ == "GObject":
            def_name = "class"
        else:
            def_name = "interface"

        name = self._abs_package_name()
        if name:
            name += "::" + self.defined_in.name
        else:
            name = self.defined_in.name
            
        return "<Method '%s' defined in %s '%s'>" % (
            self.method.name, def_name, name
        )
