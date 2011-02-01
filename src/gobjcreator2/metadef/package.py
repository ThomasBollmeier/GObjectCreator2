class PackageElement(object):

    def __init__(self,
                 name,
                 package=None):

        self._name = name
        if package is not None:
            self._package = package
        elif self is not Package.get_top():
            self._package = Package.get_top()
        else:
            self._package = None

        if self._package:
            self._package._elements[name] = self

    def _get_name(self):

        return self._name

    name = property(_get_name)

    def _get_package(self):

        return self._package

    package = property(_get_package)

class Package(PackageElement):

    TOP = None

    @staticmethod
    def get_top():

        if not Package.TOP:
            Package("", None)

        return Package.TOP

    def __init__(self,
                 name,
                 package = None):

        if package is None:
            if Package.TOP is not None:
                parent = Package.TOP
            elif not name:
                parent = None
                Package.TOP = self
            else:
                parent = Package.get_top()
        else:
            parent = package

        self._elements = {}
        
        PackageElement.__init__(self, name, parent)

    def _get_elements(self):

        return self._elements

    elements = property(_get_elements)

    def __getitem__(self, element_name):

        return self._selements[element_name]