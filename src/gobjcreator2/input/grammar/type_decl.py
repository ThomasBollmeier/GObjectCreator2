#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import GTYPE, ID, SEMICOLON

class TypeDecl(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'gtype', ident)
        
    def expand(self, start, end, context):
        
        node = start.connect(tnode(GTYPE)).connect(tnode(ID, 'name'))
        node.connect(tnode(SEMICOLON)).connect(end)
        
    def transform(self, astNode):
        
        return AstNode(self.getName(), astNode.getChildById('name').getText())
        