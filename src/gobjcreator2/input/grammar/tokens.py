#! coding=UTF-8

from tbparser.token import Word, Separator, Prefix

def register(tokenType):
    
    TOKEN_TYPES.append(tokenType)
    
    return tokenType
    
TOKEN_TYPES = []

PACKAGE = register(Word('package'))
GOBJECT = register(Word('gobject'))
GINTERFACE = register(Word('ginterface'))
ERROR_DOMAIN = register(Word('gerror'))
ENUMERATION = register(Word('genum'))
FLAGS = register(Word('gflags'))
GTYPE = register(Word('gtype'))
INCLUDE = register(Word('include'))

SUPER = register(Word('super'))
ABSTRACT = register(Word('abstract'))
PREFIX = register(Word('prefix'))
IMPLEMENTS = register(Word('implements'))

ID = register(Word('[a-zA-Z_][a-zA-Z_0-9]*'))
STRING = register(Word('"[^"]*"'))
ANY = register(Word('.*'))

BRACE_OPEN = register(Separator('{'))
BRACE_CLOSE = register(Separator('}'))
SEMICOLON = register(Separator(';'))
NAMESPACE_SEP = register(Separator('::', False))
NAMESPACE_ROOT_SEP = register(Prefix('::'))