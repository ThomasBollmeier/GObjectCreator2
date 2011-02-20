from gobjcreator2.metadef.package import PackageElement
from gobjcreator2.metadef.types import Type
from gobjcreator2.metadef.exceptions import DefinitionError
from gobjcreator2.metadef.method_info import MethodInfo
from gobjcreator2.metadef.constants import MethodInheritance

class GObject(PackageElement, Type):

    def __init__(self,
                 name,
                 package = None,
                 super_class = None):

        PackageElement.__init__(self, name, package)
        Type.__init__(self)

        self._super_class = super_class
        self.abstract = False
        self.prefix = name.lower() # prefix to be used in functions

        self._interfaces = {}
        self._attributes = {}
        self.constructor = None
        self._methods = {}
        self._overridden = {} # method info for overridden methods
        self._properties = {}
        self._signals = {}

    def get_name(self):

        return self.name

    def set_super_class(self, super_class):

        self._super_class = super_class

    def implement(self, interface):

        self._interfaces[interface.name] = interface

    def add_attribute(self, attribute):

        self._attributes[attribute.name] = attribute

    def add_method(self, method):

        self._methods[method.name] = method
        
    def override(self, method_name):

        method_info = self.lookup_method(method_name)
        if not method_info:
            raise DefinitionError("Method '%s' could not be found" % method_name)

        if method_info.method.inheritance_mode == MethodInheritance.FINAL:
            raise DefinitionError("Final method '%s' must not be overridden" % method_name)

        self._overridden[method_name] = method_info

    def add_property(self, property):

        self._properties[property.name] = property

    def add_signal(self, signal):

        self._signals[signal.name] = signal

    def lookup_method(self, method_name):
        """
        -> method_name : Name of method to lookup
        <- method info
        """
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

    # Properties:

    def _get_interfaces(self):

        return [value for value in self._interfaces.values()]

    interfaces = property(_get_interfaces)

    def _get_attributes(self):

        return [value for value in self._attributes.values()]

    attributes = property(_get_attributes)

    def _get_methods(self):

        return [value for value in self._methods.values()]

    methods = property(_get_methods)

    def _get_properties(self):

        return [value for value in self._properties.values()]

    properties = property(_get_properties)

    def _get_signals(self):

        return [value for value in self._signals.values()]

    signals = property(_get_signals)
