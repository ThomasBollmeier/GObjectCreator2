from gobjcreator2.metadef.package import PackageElement
from gobjcreator2.metadef.types import Type

class GEnum(PackageElement, Type):

    def __init__(self, name, package=None, is_external=False):

        PackageElement.__init__(self, name, package, is_external)
        Type.__init__(self)

        self.code_values = []
        
    def add_code(self, code, value=None):

        self.code_values.append((code, value))
