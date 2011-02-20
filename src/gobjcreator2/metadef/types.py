from gobjcreator2.metadef.package import PackageElement, Package

class Type(object):

    def __init__(self):

        pass

    def get_name(self):

        pass

class RefType(Type):

    def __init__(self, ref_type):

        Type.__init__(self)
        self.ref_type = ref_type

    def get_name(self):

        return "Ref_to_%s" % self.ref_type.get_name()

class ListType(Type):

    def __init__(self, line_type):

        Type.__init__(self)
        self.line_type = line_type

    def get_name(self):

        return "Line_of_%s" % self.line_type.get_name()

# simple types:

class SimpleType(Type, PackageElement):

    def __init__(self, name):

        PackageElement.__init__(self, name)

    def get_name(self):

        return self.name

class Null(SimpleType):

    def __init__(self):

        SimpleType.__init__(self, "null")

NULL = Null()

class String(SimpleType):

    def __init__(self, max_length = 0):

        if not max_length:
            name = "string"
        else:
            name = "char[%d]" % max_length

        SimpleType.__init__(self, name)

        self.max_length = max_length

STRING = String()

class Boolean(SimpleType):

    def __init__(self):

        SimpleType.__init__(self, "bool")

BOOL = Boolean()
    
class Integer(SimpleType):

    def __init__(self, signed = True):

        if signed:
            name = "int"
        else:
            name = "uint"

        SimpleType.__init__(self, name)

        self.signed = signed

INT = Integer()
UNSIGNED_INT = Integer(signed = False)

class Long(SimpleType):

    def __init__(self, signed = True):

        if signed:
            name = "long"
        else:
            name = "ulong"

        SimpleType.__init__(self, name)

        self.signed = signed

LONG = Long()
UNSIGNED_LONG = Long(signed = False)

class Float(SimpleType):

    def __init__(self):

        SimpleType.__init__(self, "float")

FLOAT = Float()

class Double(SimpleType):

    def __init__(self):

        SimpleType.__init__(self, "double")

DOUBLE = Double()

class Pointer(SimpleType):

    def __init__(self):

        SimpleType.__init__(self, "pointer")

POINTER = Pointer()
