class Property(object):

    def __init__(self,
        name,
        type,
        access,
        description,
        gtype,
        min,
        max,
        default,
        auto_create
        ):

        self.name = name
        self.type = type
        self.access = access
        self.description = description
        self.gtype = gtype
        self.min = min
        self.max = max
        self.default = default
        self.auto_create = auto_create

class PropType:

    BOOLEAN = 1
    INTEGER = 2
    FLOAT = 3
    DOUBLE = 4
    STRING = 5
    POINTER = 6
    OBJECT = 7
    ENUMERATION = 8

class PropAccess:

    READ_ONLY = 1
    INITIAL_WRITE = 2
    READ_WRITE = 3

class PropGTypeValue(object):

    def __init__(self, name, is_typename):

        self.name = name
        self.is_typename = is_typename
        
class PropValue(object):
    
    def __init__(self, name, is_codename):
        
        self.name = name
        self.is_codename = is_codename
