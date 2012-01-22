#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, connector, oneToMany, \
Switch, Condition
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.method import Method, Parameter, Signal
from gobjcreator2.input.grammar.attribute import Attribute
from gobjcreator2.input.grammar.property import Property
from gobjcreator2.input.grammar.type_name import TypePath
from gobjcreator2.input.grammar.misc_rules import ComposedId, LiteralOrCode, Prefix
import gobjcreator2.input.grammar.util as util

class ClassDef(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'gobject', ident)
        
    def expand(self, start, end, context):
        
        start_ = connector()
        end_ = connector()
        
        clsNameNode = tnode(ID, 'classname')
        clsNameNode.setEnvChange(self._onClassNameAccepted, 
                                 self._onClassNameRejected
                                 )
        
        start\
        .connect(tnode(GOBJECT))\
        .connect(clsNameNode)\
        .connect(tnode(BRACE_OPEN))\
        .connect(start_)
        
        switch = Switch({
                         SUPER: Super('super'),
                         ABSTRACT: Abstract('abstract'),
                         FINAL: Final('final'),
                         PREFIX: Prefix('prefix'),
                         IMPLEMENTS: Implements('implements'),
                         #CONSTRUCTOR: Constructor('constructor'),
                         METHOD: Method('method'),
                         OVERRIDE: Override('override'),
                         ATTRIBUTE: Attribute('attr'),
                         PROPERTY: Property('prop'),
                         SIGNAL: Signal('signal')
                         })
        start_.connect(switch).connect(start_)
        start_.connect(Constructor('constructor')).connect(start_)
        start_.connect(end_)
                 
        end_.connect(tnode(BRACE_CLOSE)).connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = astNode.getChildById('classname')
        res.addChild(AstNode('name', nameNode.getText()))
        
        self._addOptionalChild(res, astNode, 'super')
        self._addOptionalChild(res, astNode, 'abstract')
        self._addOptionalChild(res, astNode, 'final')
        self._addOptionalChild(res, astNode, 'prefix')
        self._addOptionalChildren(res, astNode, 'implements')
        self._addOptionalChild(res, astNode, 'constructor')
        self._addOptionalChildren(res, astNode, 'method')
        self._addOptionalChildren(res, astNode, 'override')
        self._addOptionalChildren(res, astNode, 'attr')
        self._addOptionalChildren(res, astNode, 'prop')
        self._addOptionalChildren(res, astNode, 'signal')
        
        return res
    
    def _addOptionalChild(self, parent, astNode, ident):
        
        node = astNode.getChildById(ident)
        if node:
            node.setId('')
            parent.addChild(node)

    def _addOptionalChildren(self, parent, astNode, ident):
        
        nodes = astNode.getChildrenById(ident)
        for node in nodes:
            node.setId('')
            parent.addChild(node)      
            
    def _onClassNameAccepted(self, envVars, token, node):
        
        if token:
            envVars['GOBJECT'] = token.getText()
    
    def _onClassNameRejected(self, envVars, token, node):
        
        if token:
            envVars['GOBJECT'] = ''
          
class Super(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'super', ident)
        
    def expand(self, start, end, context):
        
        start\
        .connect(tnode(SUPER))\
        .connect(TypePath('typePath'))\
        .connect(tnode(SEMICOLON))\
        .connect(end)
        
    def transform(self, astNode):
        
        return AstNode(self.getName(), astNode.getChildById('typePath').getText())
        
class Abstract(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'abstract', ident)
        
    def expand(self, start, end, context):
        
        start.connect(tnode(ABSTRACT)).connect(tnode(SEMICOLON)).connect(end)
        
    def transform(self, astNode):
        
        return AstNode(self.getName())

class Final(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'final', ident)
        
    def expand(self, start, end, context):
        
        start.connect(tnode(FINAL)).connect(tnode(SEMICOLON)).connect(end)
        
    def transform(self, astNode):
        
        return AstNode(self.getName())
    
class Implements(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'implements', ident)
        
    def expand(self, start, end, context):
        
        start\
        .connect(tnode(IMPLEMENTS))\
        .connect(TypePath('interfaceName'))\
        .connect(tnode(SEMICOLON))\
        .connect(end)
        
    def transform(self, astNode):
        
        node = astNode.getChildById('interfaceName')
        
        return AstNode(self.getName(), node.getText())
    
class Constructor(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'constructor', ident)
        
        self.setEnvVar('CONSTRUCTOR', True)
        
    def expand(self, start, end, context):
                
        start_ = connector()
        end_ = connector()
        braceOpen = tnode(BRACE_OPEN)
        
        start.connect(tnode(CONSTRUCTOR)).connect(braceOpen)
        start.connect(Condition(self._isConstructorName)).connect(tnode(ID)).connect(braceOpen)
        braceOpen.connect(start_)
        
        start_.connect(Parameter('parameter')).connect(start_)
        start_.connect(InitProperties('initProps')).connect(start_)
        start_.connect(end_)
        
        end_.connect(tnode(BRACE_CLOSE)).connect(end)
            
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        for node in astNode.getChildrenById('parameter'):
            node.setId('')
            res.addChild(node)
            
        node = astNode.getChildById('initProps')
        if node:
            node.setId('')
            res.addChild(node)
        
        return res
    
    def _isConstructorName(self, context):
        
        if context.token:
            return context.token.getText() == context.getEnvVar('GOBJECT')
        else:
            return False
    
class InitProperties(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'initProperties', ident)
        
    def expand(self, start, end, context):
        
        start\
        .connect(tnode(INIT_PROPERTIES))\
        .connect(tnode(BRACE_OPEN))\
        .connect(oneToMany(InitProperty('init')))\
        .connect(tnode(BRACE_CLOSE))\
        .connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        for initNode in astNode.getChildrenById('init'):
            initNode.setId('')
            res.addChild(initNode)
        
        return res
    
class InitProperty(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'initProperty', ident)
        
    def expand(self, start, end, context):
        
        start\
        .connect(ComposedId('name'))\
        .connect(tnode(COLON))\
        .connect(LiteralOrCode('value'))\
        .connect(tnode(SEMICOLON))\
        .connect(end)
                       
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = AstNode('name', astNode.getChildById('name').getText())
        res.addChild(nameNode)
        
        util.addChild(astNode, res, 'value')
        
        return res       
    
class Override(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'override', ident)
        
    def expand(self, start, end, context):
        
        start\
        .connect(tnode(OVERRIDE))\
        .connect(tnode(ID, 'name'))\
        .connect(tnode(SEMICOLON))\
        .connect(end)
        
    def transform(self, astNode):
        
        methodName = astNode.getChildById('name').getText()
        
        return AstNode(self.getName(), methodName)
        
