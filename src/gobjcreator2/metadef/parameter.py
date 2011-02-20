class Parameter(object):

    def __init__(self,
                 name,
                 type,
                 modifiers=[]):

        self.name = name
        self.type = type
        self.modifiers = modifiers

class ConstructorParameter(Parameter):

    def __init__(self,
                 name,
                 type,
                 modifiers=[],
                 bind_to=""):

        Parameter.__init__(self, name, type, modifiers)
        self.bind_to = bind_to
