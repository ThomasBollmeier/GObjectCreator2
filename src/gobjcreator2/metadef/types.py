# built-in types:

class Type(object):

    def __init__(self):

        pass

    def get_name(self):

        pass

class BuiltInType(Type):

    def __init__(self, name):

        self._name = name

    def get_name(self):

        return self._name

class Null(BuiltInType):

    def __init__(self):

        BuiltInType.__init__(self, "NULL")

NULL = Null()

class String(BuiltInType):

    def __init__(self, max_length = 0):

        if not max_length:
            name = "string"
        else:
            name = "char[%d]" % max_length

        BuiltInType.__init__(self, name)

        self.max_length = max_length

class Boolean(BuiltInType):

    def __init__(self):

        BuiltInType.__init__(self, "bool")

BOOL = Boolean()
    
class Integer(BuiltInType):

    def __init__(self, signed = True):

        BuiltInType.__init__(self, "int")

        self.signed = signed

INT = Integer()
UNSIGNED_INT = Integer(signed = False)

class Float(BuiltInType):

    def __init__(self):

        BuiltInType.__init__(self, "float")

FLOAT = Float()

class Double(BuiltInType):

    def __init__(self):

        BuiltInType.__init__(self, "double")

DOUBLE = Double()