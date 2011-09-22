#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, sequence, zeroToOne, zeroToMany
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import ID, NAMESPACE_SEP, NAMESPACE_ROOT_SEP

class TypePath(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'typePath', ident)
        
    def expand(self, start, end, context):
        
        s1 = sequence(tnode(NAMESPACE_ROOT_SEP), tnode(ID), tnode(NAMESPACE_SEP))
        s2 = sequence(tnode(ID), tnode(NAMESPACE_SEP))
        
        start\
        .connect(zeroToOne(s1))\
        .connect(zeroToMany(s2))\
        .connect(tnode(ID))\
        .connect(end)
        
    def transform(self, astNode):
        
        typePath = ""
        for child in astNode.getChildren():
            typePath += child.getText()
            
        return AstNode(self.getName(), typePath)