from gobjcreator2.metadef.method import Method, MethodInheritance
from gobjcreator2.metadef.constants import Scope, Visibility

class Constructor(Method):

    NAME = "new"

    def __init__(self,
                 cls,
                 ):

        Method.__init__(self,
                        Constructor.NAME,
                        result = cls,
                        result_modifiers = [],
                        visibility = Visibility.PUBLIC,
                        scope = Scope.STATIC,
                        inheritance_mode = MethodInheritance.FINAL
                        )

        self.property_inits = {}

    def init_property(self, name, value, is_code_value):

        self.property_inits[name] = (value, is_code_value)
