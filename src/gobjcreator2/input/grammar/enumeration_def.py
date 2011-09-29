#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, oneToMany
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import ENUMERATION, ID, BRACE_OPEN, BRACE_CLOSE
from gobjcreator2.input.grammar.misc_rules import Code
import gobjcreator2.input.grammar.util as util

class EnumerationDef(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'genum', ident)
        
        self.setEnvVar('ENUMERATION', True)
                
    def expand(self, start, end, context):
        
        start\
        .connect(tnode(ENUMERATION))\
        .connect(tnode(ID, 'name'))\
        .connect(tnode(BRACE_OPEN))\
        .connect(oneToMany(Code('code')))\
        .connect(tnode(BRACE_CLOSE))\
        .connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = astNode.getChildById('name')
        res.addChild(AstNode('name', nameNode.getText()))
        
        util.addOptionalChildren(astNode, res, 'code')
        
        return res