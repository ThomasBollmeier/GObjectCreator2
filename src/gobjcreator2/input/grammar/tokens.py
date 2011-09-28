#! coding=UTF-8

from tbparser.token import Keyword, Word, Separator, Prefix, Literal

TOKEN_TYPES = []

def register(tokenType):
    
    TOKEN_TYPES.append(tokenType)
    
    return tokenType

def addKeyword(kw):
    
    return register(Keyword(kw))

PACKAGE = addKeyword('package')
GOBJECT = addKeyword('gobject')
GINTERFACE = addKeyword('ginterface')
ERROR_DOMAIN = addKeyword('gerror')
ENUMERATION = addKeyword('genum')
FLAGS = addKeyword('gflags')
GTYPE = addKeyword('gtype')
INCLUDE = addKeyword('include')

SUPER = addKeyword('super')
ABSTRACT = addKeyword('abstract')
PREFIX = addKeyword('prefix')
IMPLEMENTS = addKeyword('implements')
CONSTRUCTOR = addKeyword('constructor')
METHOD = addKeyword('method')
OVERRIDE = addKeyword('override')
ATTRIBUTE = addKeyword('attribute')
PROPERTY = addKeyword('property')
SIGNAL = addKeyword('signal')
RESULT = addKeyword('result')
VISI = addKeyword('visibility')
PUBLIC = addKeyword('public')
PROTECTED = addKeyword('protected')
PRIVATE = addKeyword('private')
SCOPE = addKeyword('scope')
INSTANCE = addKeyword('instance')
STATIC = addKeyword('static')
INHERITANCE = addKeyword('inheritance')
FINAL = addKeyword('final')
VIRTUAL = addKeyword('virtual')
PARAMETER = addKeyword('parameter')
TYPE = addKeyword('type')
UNSIGNED = addKeyword('unsigned')
INTEGER = addKeyword('integer')
LONG = addKeyword('long')
NULL = addKeyword('null')
BOOLEAN = addKeyword('boolean')
STRING = addKeyword('string')
FLOAT = addKeyword('float')
DOUBLE = addKeyword('double')
POINTER = addKeyword('pointer')
PROP_TYPE_OBJECT = addKeyword('object')
PROP_TYPE_ENUMERATION = addKeyword('enumeration') 
ACCESS = addKeyword('access')
DESCRIPTION = addKeyword('description')
GTYPENAME = addKeyword('gtypename')
PROP_MAX = addKeyword('max')
PROP_MIN = addKeyword('min')
PROP_DEFAULT = addKeyword('default')
AUTO_CREATE = addKeyword('auto_create')
READ = register(Word('read'))
WRITE = register(Word('write'))
ONLY = register(Word('only'))
INITIAL = register(Word('initial'))
MODIFIERS = addKeyword('modifiers')
CONST = addKeyword('const')
REF = addKeyword('ref')
LIST = addKeyword('list')
BIND_PROPERTY = addKeyword('bind_property')
INIT_PROPERTIES = addKeyword('init_properties')

ID = register(Word('[a-zA-Z_][a-zA-Z_0-9]*'))
LITERAL = register(Literal.get())
ANY = register(Word('.*'))

DOT = register(Separator('.', False))
DASH = register(Separator('-'))
BRACE_OPEN = register(Separator('{'))
BRACE_CLOSE = register(Separator('}'))
PAR_OPEN = register(Separator('\('))
PAR_CLOSE = register(Separator('\)'))
COLON = register(Separator.create('\A([^:]*)(:)([^:])*\Z'))
SEMICOLON = register(Separator(';'))
NAMESPACE_SEP = register(Separator('::', False))
NAMESPACE_ROOT_SEP = register(Prefix('::'))