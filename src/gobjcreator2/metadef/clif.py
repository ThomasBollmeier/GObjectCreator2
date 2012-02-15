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

from gobjcreator2.metadef.package import PackageElement
from gobjcreator2.metadef.types import Type

class ClsIntf(PackageElement, Type):
    
    def __init__(self,
                 name,
                 package = None,
                 is_external = False
                 ):

        PackageElement.__init__(self, name, package, is_external)
        Type.__init__(self)
        
        self._methods = {}
        self._method_order = []
        
    def add_method(self, method):
    
        if method.name in self._methods:
            self._method_order.remove(self._method[method.name])

        self._methods[method.name] = method
        self._method_order.append(method)

    def supports_further_params(self):

        for method in self._methods.values():
            if method.supportsFurtherParams:
                return True
            
        return False

    def _get_methods(self):
        
        return self._method_order[:]
    
    methods = property(_get_methods)
