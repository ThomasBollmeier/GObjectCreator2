#! coding=UTF-8

from tbparser.grammar import Grammar, Switch
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.package_def import PackageDef
from gobjcreator2.input.grammar.class_def import ClassDef
from gobjcreator2.input.grammar.intf_def import InterfaceDef
from gobjcreator2.input.grammar.error_domain_def import ErrorDomainDef
from gobjcreator2.input.grammar.enumeration_def import EnumerationDef
from gobjcreator2.input.grammar.flags_def import FlagsDef
from gobjcreator2.input.grammar.type_decl import TypeDecl
from gobjcreator2.input.grammar.include_stmt import IncludeStmt

class GOCGrammar(Grammar):
    
    def __init__(self):
        
        Grammar.__init__(self, TOKEN_TYPES)
        
    def expand(self, start, end, context):
        
        switch = Switch({
                         PACKAGE: PackageDef(),
                         GOBJECT: ClassDef(),
                         GINTERFACE: InterfaceDef(),
                         ERROR_DOMAIN: ErrorDomainDef(),
                         ENUMERATION: EnumerationDef(),
                         FLAGS: FlagsDef(),
                         GTYPE: TypeDecl(),
                         INCLUDE: IncludeStmt()
                         })
        
        start.connect(switch).connect(start)
        start.connect(end)
