#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, Switch, zeroToMany
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.method import Method, Signal
from gobjcreator2.input.grammar.misc_rules import Prefix as PrefixRule
import gobjcreator2.input.grammar.util as util

class InterfaceDef(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'ginterface', ident)
        
    def expand(self, start, end, context):
        
        branches = {
                    METHOD: Method('method'),
                    SIGNAL: Signal('signal'),
                    PREFIX: PrefixRule('prefix')
                    }
        
        start\
        .connect(tnode(GINTERFACE))\
        .connect(tnode(ID, 'interfaceName'))\
        .connect(tnode(BRACE_OPEN))\
        .connect(zeroToMany(Switch(branches)))\
        .connect(tnode(BRACE_CLOSE))\
        .connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = astNode.getChildById('interfaceName')
        res.addChild(AstNode('name', nameNode.getText()))
        
        util.addOptionalChild(astNode, res, 'prefix')
        util.addOptionalChildren(astNode, res, 'method')
        util.addOptionalChildren(astNode, res, 'signal')
        
        return res