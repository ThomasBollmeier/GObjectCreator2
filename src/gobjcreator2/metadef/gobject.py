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
from gobjcreator2.metadef.types import Type, BOOL, BYTE, INT,\
FLOAT, DOUBLE, STRING
from gobjcreator2.metadef.exceptions import DefinitionError
from gobjcreator2.metadef.method_info import MethodInfo
from gobjcreator2.metadef.constants import MethodInheritance, Visibility
from gobjcreator2.metadef.constructor import Constructor
from gobjcreator2.metadef.attribute import Attribute
from gobjcreator2.metadef.property import PropType

class GObject(ClsIntf):

    def __init__(self,
                 name,
                 package = None,
                 super_class = None,
                 is_external = False
                 ):

        ClsIntf.__init__(self, name, package, is_external)
        
        self._super_class = super_class
        self.abstract = False
        self.final = False
        self.prefix = name # prefix to be used in functions

        self._interfaces = {}
        self._attributes = {}
        self.constructor = Constructor(self)
        self._overridden = {} # method info for overridden methods
        self._properties = {}
        self._signals = {}
        
    def get_name(self):

        return self.name
    
    def set_super_class(self, super_class):

        self._super_class = super_class

    def get_super_class(self):

        return self._super_class

    super_class = property(get_super_class, set_super_class)

    def implement(self, interface):

        self._interfaces[interface.name] = interface

    def add_attribute(self, attribute):
        
        if self.final and attribute.visibility == Visibility.PROTECTED:
            raise DefinitionError("Final classes must not have protected attributes")

        self._attributes[attribute.name] = attribute
        
    def add_method(self, method):
        
        if self.final:
            if method.visibility == Visibility.PROTECTED:
                raise DefinitionError("Final classes must not have protected methods")
            elif method.inheritance_mode != MethodInheritance.FINAL:
                raise DefinitionError("Final classes must not have abstract or virtual methods")
                
        ClsIntf.add_method(self, method)
                        
    def override(self, method_name):

        method_info = self.lookup_method(method_name)
        if not method_info:
            raise DefinitionError("Method '%s' could not be found" % method_name)

        if method_info.method.inheritance_mode == MethodInheritance.FINAL:
            raise DefinitionError("Final method '%s' must not be overridden" % method_name)

        self._overridden[method_name] = method_info

    def add_property(self, property):

        self._properties[property.name] = property
        
        if property.auto_create:
            # Create attribute that holds property value:
            attr_name = property.name.replace("-", "_")
            
            if not hasattr(self, "_prop_type_map"):
                self._prop_type_map = {
                                       PropType.BOOLEAN: BOOL,
                                       PropType.BYTE: BYTE,
                                       PropType.INTEGER: INT,
                                       PropType.FLOAT: FLOAT,
                                       PropType.DOUBLE: DOUBLE,
                                       PropType.STRING: STRING,
                                       }
            try:
                attr_type = self._prop_type_map[property.type]
            except KeyError:
                raise DefinitionError("Auto-creation of attribute not supported for property %s" % \
                                 property.name)
            
            self.add_attribute(Attribute(attr_name, attr_type))
            
    def add_signal(self, signal):

        self._signals[signal.name] = signal

    def lookup_method(self, method_name, interface_name=""):
        """
        -> method_name : Name of method to lookup
        <- method info
        """
        if not interface_name:
            
            if method_name in self._methods:
                method = self._methods[method_name]
                return MethodInfo(method, self)
    
            for interface in self._interfaces.values():
                for interface_method in interface.methods:
                    if method_name == interface_method.name:
                        return MethodInfo(interface_method, interface)
    
            if self._super_class:
                return self._super_class.lookup_method(method_name)
            else:
                return None
            
        else:
            
            for method in self._interfaces[interface_name].methods:
                if method.name == method_name:
                    return MethodInfo(method, self._interfaces[interface_name])
            return None

    def has_attributes(self, visibility, scope=None):

        for value in self._attributes.values():
            if value.visibility == visibility:
                if scope is None:
                    return True
                elif value.scope == scope:
                    return True
            
        return False

    # Properties:

    def _get_interfaces(self):

        return [value for value in self._interfaces.values()]

    interfaces = property(_get_interfaces)

    def _get_attributes(self):

        return [value for value in self._attributes.values()]

    attributes = property(_get_attributes)

    def _get_properties(self):

        return [value for value in self._properties.values()]

    properties = property(_get_properties)

    def _get_signals(self):

        return [value for value in self._signals.values()]

    signals = property(_get_signals)

    def _get_overridden(self):

        return [method_info for method_info in self._overridden.values()]

    overridden_methods = property(_get_overridden)