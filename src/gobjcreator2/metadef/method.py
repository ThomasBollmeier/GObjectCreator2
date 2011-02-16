from gobjcreator2.metadef.enums import \
    Visibility, Scope, MethodInheritance
from gobjcreator2.metadef.types import NULL

class Method(object):

    def __init__(self,
                 name,
                 result = NULL,
                 result_modifiers = [],
                 visibility = Visibility.PUBLIC,
                 scope = Scope.INSTANCE,
                 inheritance_mode = MethodInheritance.FINAL
                 ):

        self.name = name
        self.result = result
        self.result_modifiers = result_modifiers
        self.visibility = visibility
        self.scope = scope
        self.inheritance_mode = inheritance_mode
        self.parameters = []

    def add_parameter(self, param):

        self.parameters.append(param)

class InterfaceMethod(Method):

    def __init__(self,
                 name,
                 result = NULL,
                 result_modifiers = []
                 ):

        Method.__init__(self, name, result, result_modifiers,
                        Visibility.PUBLIC, Scope.INSTANCE,
                        MethodInheritance.ABSTRACT)