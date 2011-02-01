from gobjcreator2.metadef.package import PackageElement
from gobjcreator2.metadef.types import Type

class GInterface(PackageElement, Type):

    def __init__(self,
                 name,
                 package = None):

        PackageElement.__init__(self, name, package)
        Type.__init__(self)

        self._methods = {}
        self._signals = {}

    def get_name(self):

        return self.name

    def add_method(self, method):

        self._methods[method.name] = method

    def add_signal(self, signal):

        self._signals[signal.name] = signal

    # Properties

    def _get_methods(self):

        return [m for m in self._methods.values()]

    methods = property(_get_methods)

    def _get_signals(self):

        return [s for s in self._signals.values()]

    signals = property(_get_signals)
