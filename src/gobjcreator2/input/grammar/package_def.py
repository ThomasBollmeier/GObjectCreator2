#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, connector
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import PACKAGE, ID, BRACE_OPEN, BRACE_CLOSE
from gobjcreator2.input.grammar.class_def import ClassDef
from gobjcreator2.input.grammar.intf_def import InterfaceDef
from gobjcreator2.input.grammar.error_domain_def import ErrorDomainDef
from gobjcreator2.input.grammar.enumeration_def import EnumerationDef
from gobjcreator2.input.grammar.flags_def import FlagsDef
from gobjcreator2.input.grammar.type_decl import TypeDecl

class PackageDef(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'package', ident)
        
    def expand(self, start, end, context):
        
        start_ = connector()
        end_ = connector()
        
        start\
        .connect(tnode(PACKAGE))\
        .connect(tnode(ID, 'name'))\
        .connect(tnode(BRACE_OPEN))\
        .connect(start_)
        
        self._connect_branch(PackageDef('content'), start_, end_)
        self._connect_branch(ClassDef('content'), start_, end_)
        self._connect_branch(InterfaceDef('content'), start_, end_)
        self._connect_branch(ErrorDomainDef('content'), start_, end_)
        self._connect_branch(EnumerationDef('content'), start_, end_)
        self._connect_branch(FlagsDef('content'), start_, end_)
        self._connect_branch(TypeDecl('content'), start_, end_)
        
        end_.connect(tnode(BRACE_CLOSE)).connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        res.addChild(AstNode('name', astNode.getChildById('name').getText()))
        
        for child in astNode.getChildrenById('content'):
            child.setId('')
            res.addChild(child)
        
        return res
        
    def _connect_branch(self, branch, start, end):
        
        start.connect(branch)
        branch.connect(end)
        branch.connect(start)