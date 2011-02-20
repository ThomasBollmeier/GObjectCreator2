class Signal(object):

    def __init__(self,
                 name,
                 result):

        self.name = name
        self.internal_name = name.replace("-", "_")
        self.result = result
        self.parameters = []

    def add_parameter(self, name, type):

        self.parameters.append((name, type))

class SignalType:

    NULL = 1
    BOOLEAN = 2
    INTEGER = 3
    FLOAT = 4
    DOUBLE = 5
    STRING = 6
    POINTER = 7
    OBJECT = 8
    ENUMERATION = 9
