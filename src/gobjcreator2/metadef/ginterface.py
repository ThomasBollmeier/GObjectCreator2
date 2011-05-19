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


from gobjcreator2.metadef.clif import ClsIntf
from gobjcreator2.metadef.method_info import MethodInfo

class GInterface(ClsIntf):

    def __init__(self,
                 name,
                 package = None,
                 is_external = False
                 ):

        ClsIntf.__init__(self, name, package, is_external)
        
        self.prefix = name # prefix used in function names

        self._signals = {}
        
    def get_name(self):

        return self.name

    def add_signal(self, signal):

        self._signals[signal.name] = signal

    def lookup_method(self, method_name, interface_name=""):
        """
        -> method_name : Name of method to lookup
        <- method info
        """
        if interface_name and interface_name != self.name:
            return None
            
        if method_name not in self._methods:
            return None
        
        method = self._methods[method_name]
    
        return MethodInfo(method, self)
    
    # Properties

    def _get_signals(self):

        return [s for s in self._signals.values()]

    signals = property(_get_signals)
