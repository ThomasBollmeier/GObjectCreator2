from gobjcreator2.metadef.types import Type
from gobjcreator2.metadef.package import PackageElement

class GType(PackageElement, Type):

    def __init__(self, name, package=None):

        PackageElement.__init__(self, name, package)
        Type.__init__(self)

    def get_name(self):

        return self.name
