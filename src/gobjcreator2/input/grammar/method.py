#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, \
connector, sequence, zeroToOne, Switch, oneToMany
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.type_name import TypeName
from gobjcreator2.input.grammar.misc_rules import ComposedId, \
Visibility, Inheritance, Scope, Type
import gobjcreator2.input.grammar.util as util

class Method(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'method', ident)
        
    def expand(self, start, end, context):
        
        start_ = connector()
        
        branches = {}
        branches[PARAMETER] = Parameter('parameter')
        branches[RESULT] = Result('result')
        
        if not context.getEnvVar('INTERFACE'):
            
            branches[VISI] = Visibility('visi')
            branches[INHERITANCE] = Inheritance('inh')
            branches[SCOPE] = Scope('scope')
        
        start\
        .connect(tnode(METHOD))\
        .connect(tnode(ID, 'name'))\
        .connect(tnode(BRACE_OPEN))\
        .connect(start_)
        
        start_.connect(Switch(branches)).connect(start_)
        start_\
        .connect(zeroToOne(sequence(tnode(FURTHER_PARAMETERS, 'further_params'), tnode(SEMICOLON))))\
        .connect(tnode(BRACE_CLOSE))\
        .connect(end)
    
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = AstNode('name', astNode.getChildById('name').getText())
        res.addChild(nameNode)
            
        util.addOptionalChildren(astNode, res, 'parameter')
        util.addOptionalChild(astNode, res, 'result')
        util.addOptionalChild(astNode, res, 'visi')
        util.addOptionalChild(astNode, res, 'inh')
        util.addOptionalChild(astNode, res, 'scope')

        node = astNode.getChildById('further_params')
        if node:
            res.addChild(AstNode('further_params'))
 
        return res
    
class Signal(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'signal', ident)
        
    def expand(self, start, end, context):
        
        branches = {
                    PARAMETER: Parameter('parameter'),
                    RESULT: Result('result')
                    }       
        
        start\
        .connect(tnode(SIGNAL))\
        .connect(ComposedId('name'))\
        .connect(tnode(BRACE_OPEN))\
        .connect(oneToMany(Switch(branches)))\
        .connect(tnode(BRACE_CLOSE))\
        .connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = AstNode('name', astNode.getChildById('name').getText())
        res.addChild(nameNode)
        
        util.addOptionalChild(astNode, res, 'result')
        util.addOptionalChildren(astNode, res, 'parameter')
        
        return res
    
class Parameter(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'parameter', ident)
        
    def expand(self, start, end, context):
        
        start_ = connector()
        end_ = connector()
        
        start\
        .connect(tnode(PARAMETER))\
        .connect(tnode(ID, 'name'))\
        .connect(tnode(BRACE_OPEN))\
        .connect(Type('type'))\
        .connect(start_)
           
        end_.connect(tnode(BRACE_CLOSE)).connect(end)
        
        start_.connect(end_)
        
        start_\
        .connect(tnode(MODIFIERS, 'modifiers'))\
        .connect(tnode(COLON))\
        .connect(tnode(CONST, 'const'))\
        .connect(tnode(SEMICOLON))\
        .connect(start_)
        
        if context.getEnvVar('CONSTRUCTOR'):
        
            start_\
            .connect(tnode(BIND_PROPERTY, 'bindProperty'))\
            .connect(tnode(COLON))\
            .connect(ComposedId('propertyId'))\
            .connect(tnode(SEMICOLON))\
            .connect(start_)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        res.addChild(AstNode('name', astNode.getChildById('name').getText()))
        
        typeNode = astNode.getChildById('type')
        typeNode.setId('')
        res.addChild(typeNode)
        
        modifiersNode = astNode.getChildById('modifiers')
        if modifiersNode:
            res.addChild(AstNode('const'))
            
        bindNode = astNode.getChildById('bindProperty')
        if bindNode:
            propIdNode = astNode.getChildById('propertyId')
            res.addChild(AstNode('bindProperty', propIdNode.getText()))
            
        return res

class Result(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'result', ident)
        
    def expand(self, start, end, context):
        
        modifiers = sequence(tnode(MODIFIERS, 'modifiers'),
                             tnode(COLON),  
                             tnode(CONST, 'const'),
                             tnode(SEMICOLON)
                             )      
        start\
        .connect(tnode(RESULT))\
        .connect(tnode(BRACE_OPEN))\
        .connect(Type('type'))\
        .connect(zeroToOne(modifiers))\
        .connect(tnode(BRACE_CLOSE))\
        .connect(end)
                
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        typeNode = astNode.getChildById('type')
        typeNode.setId('')
        res.addChild(typeNode)
        
        modifiersNode = astNode.getChildById('modifiers')
        if modifiersNode:
            res.addChild(AstNode('const'))
                     
        return res
