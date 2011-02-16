from enums import Scope, Visibility

class Attribute(object):

    def __init__(self,
                 name,
                 type,
                 scope = Scope.INSTANCE,
                 visibility = Visibility.PRIVATE):

        self.name = name
        self.type = type
        self.scope = scope
        self.visibility = visibility

