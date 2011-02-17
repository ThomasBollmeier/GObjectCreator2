from gobjcreator2.input.reader import GOCVisitor
from gobjcreator2.metadef.package import Package
from gobjcreator2.metadef.gobject import GObject
from gobjcreator2.metadef.ginterface import GInterface
from gobjcreator2.metadef.gtype import GType
from gobjcreator2.metadef.error_domain import ErrorDomain
from gobjcreator2.metadef.genum import GEnum
from gobjcreator2.metadef.gflags import GFlags

class VisitorStep1(GOCVisitor):

    def __init__(self):

        self._package_stack = []

    def _get_package(self):

        if self._package_stack:
            return self._package_stack[-1]
        else:
            return None
        
    def package_begin(self, name):

        package = Package(name, package = self._get_package())
        self._package_stack.append(package)

    def package_end(self, name):

        self._package_stack.pop()

    def gobject_begin(self,
                      name,
                      super,
                      interfaces,
                      attrs):

        GObject(name, package = self._get_package())

    def ginterface_begin(self, name):

        GInterface(name, package = self._get_package())

    def gtype(self, name):

        GType(name, package = self._get_package())

    def error_domain(self, name, codes):

        ErrorDomain(name, package = self._get_package())

    def enumeration(self, name, codevals):

        GEnum(name, package = self._get_package())

    def flags(self, name, codes):

        GFlags(name, package = self._get_package())
