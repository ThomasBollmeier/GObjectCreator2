from gobjcreator2.metadef.package import PackageElement
from gobjcreator2.metadef.types import Type

class GFlags(PackageElement, Type):

    def __init__(self, name, package=None):

        PackageElement.__init__(self, name, package)
        Type.__init__(self)

        self.codes = []

    def add_code(self, code):

        self.codes.append(code)
