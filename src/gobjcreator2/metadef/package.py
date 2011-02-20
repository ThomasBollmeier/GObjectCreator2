from gobjcreator2.metadef.exceptions import DefinitionError

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

    _SEPARATOR = "::"

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

    def get_element(self, path):

        parts = path.split(Package._SEPARATOR)

        if len(parts) == 1:
            try:
                res = self._elements[path]
                return res
            except KeyError:
                if self is not Package.get_top():
                    try:
                        return Package.get_top()._elements[path]
                    except KeyError:
                        raise DefinitionError("Unknown element: %s" % path)
                else:
                    raise DefinitionError("Unknown element: %s" % path)
        else:
            packages = parts[:-1]
            if not packages[0]:
                # => absolute path
                abs_path = Package._SEPARATOR.join(parts[1:])
                return Package.get_top().get_element(abs_path)
            else:
                # assume it is a relative path first:
                try:
                    sub_package = self._elements[packages[0]]
                    if not isinstance(sub_package, Package):
                        raise DefinitionError("Unknown element: %s" % path)
                    sub_path = Package._SEPARATOR.join(parts[1:])
                    return sub_package.get_element(sub_path)
                except (KeyError, DefinitionError):
                    if self is not Package.get_top():
                        return Package.get_top().get_element(path)
                    else:
                        raise DefinitionError("Unknown element: %s" % path)


    def _get_elements(self):

        return self._elements

    elements = property(_get_elements)

    def __getitem__(self, element_name):

        return self.get_element(element_name)