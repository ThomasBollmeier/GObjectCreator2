#! coding=UTF-8

from tbparser.grammar import Grammar
from gobjcreator2.input.grammar.tokens import TOKEN_TYPES
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
        
        self._connect_branch(PackageDef(), start, end)
        self._connect_branch(ClassDef(), start, end)
        self._connect_branch(InterfaceDef(), start, end)
        self._connect_branch(ErrorDomainDef(), start, end)
        self._connect_branch(EnumerationDef(), start, end)
        self._connect_branch(FlagsDef(), start, end)
        self._connect_branch(TypeDecl(), start, end)
        self._connect_branch(IncludeStmt(), start, end)
        
    def _connect_branch(self, branch, start, end):
        
        start.connect(branch)
        branch.connect(end)
        branch.connect(start)