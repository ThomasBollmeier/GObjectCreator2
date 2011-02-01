from gobjcreator2.metadef.package import PackageElement

class ErrorDomain(PackageElement):

    def __init__(self,
                 name,
                 package = None):

        PackageElement.__init__(name, package)
