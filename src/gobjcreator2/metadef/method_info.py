class MethodInfo(object):

    def __init__(self,
                method,
                defined_in
                ):

        self.method = method
        self.defined_in = defined_in

    def _abs_package_name(self):

        package = self.defined_in.package
        name = package.name
        while package.package:
            package = package.package
            if package.name:
                name = package.name + "::" + name

        return name

    def __str__(self):

        if self.defined_in.__class__.__name__ == "GClass":
            def_name = "class"
        else:
            def_name = "interface"

        name = self._abs_package_name()
        if name:
            name += "::" + self.defined_in.name
        else:
            name = self.defined_in.name
            
        return "<Method '%s' defined in %s '%s'>" % (
            self.method.name, def_name, name
        )
