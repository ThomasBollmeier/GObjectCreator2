from gobjcreator2.metadef.package import PackageElement

class ErrorDomain(PackageElement):

    def __init__(self,
                 name,
                 package = None):

        PackageElement.__init__(self, name, package)

        self.error_codes = []

    def add_error_code(self, error_code):

        self.error_codes.append(error_code)
