from gobjcreator2.metadef.package import PackageElement
from gobjcreator2.metadef.types import Type
from gobjcreator2.metadef.method_info import MethodInfo

class GInterface(PackageElement, Type):

    def __init__(self,
                 name,
                 package = None):

        PackageElement.__init__(self, name, package)
        Type.__init__(self)

        self.prefix = name # prefix used in function names

        self._methods = {}
        self._signals = {}

    def get_name(self):

        return self.name

    def add_method(self, method):

        self._methods[method.name] = method

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

    def _get_methods(self):

        return [m for m in self._methods.values()]

    methods = property(_get_methods)

    def _get_signals(self):

        return [s for s in self._signals.values()]

    signals = property(_get_signals)
