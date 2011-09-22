#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, zeroToMany
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import ENUMERATION, ID, BRACE_OPEN, BRACE_CLOSE, ANY

class EnumerationDef(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'genum', ident)
        
    def expand(self, start, end, context):
        
        any = zeroToMany(tnode(ANY))
        
        node = start.connect(tnode(ENUMERATION)).connect(tnode(ID, 'name'))
        node.connect(tnode(BRACE_OPEN)).connect(any).connect(tnode(BRACE_CLOSE)).connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = astNode.getChildById('name')
        res.addChild(AstNode('name', nameNode.getText()))
        
        return res