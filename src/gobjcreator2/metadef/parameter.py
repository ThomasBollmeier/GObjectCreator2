class Parameter(object):

    def __init__(self,
                 name,
                 type,
                 modifiers=[]):

        self.name = name
        self.type = type
        self.modifiers = modifiers
