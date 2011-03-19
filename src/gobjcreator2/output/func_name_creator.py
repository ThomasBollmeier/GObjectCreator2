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


class FuncNameCreator(object):
    
    def __init__(self):
        
        self._intf_funcs = {}
        
    def create_impl_func_name(self, method_name, interface_name=""):
        
        if not interface_name:
            return method_name + "_im"
        else:
            if method_name not in self._intf_funcs:
                res = method_name + "_im"
                self._intf_funcs[method_name] = {interface_name: res}
                return res
            else:
                func_names = self._intf_funcs[method_name]
                if interface_name in func_names:
                    return func_names[interface_name]
                else:
                    res = method_name + "_%d_im" % len(func_names)
                    func_names[interface_name] = res
                    return res 
                
    def get_info(self, impl_func_name):
        
        for method_name in self._intf_funcs:
            for interface_name, func_name in self._intf_funcs[method_name].items():
                if func_name == impl_func_name:
                    return (method_name, interface_name)
        
        return (impl_func_name[:-3], "")
        