#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import INCLUDE, LITERAL

class IncludeStmt(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'include', ident)
        
    def expand(self, start, end, context):
        
        start.connect(tnode(INCLUDE)).connect(tnode(LITERAL, 'file')).connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        fileNode = astNode.getChildById('file')
        fileName = fileNode.getText().strip('"')
        res.addChild(AstNode('file', fileName))
        
        return res