#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, connector, zeroToOne
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.type_name import TypePath

class ClassDef(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'gobject', ident)
        
    def expand(self, start, end, context):
        
        start_ = connector()
        end_ = connector()
        
        start\
        .connect(tnode(GOBJECT))\
        .connect(tnode(ID, 'classname'))\
        .connect(tnode(BRACE_OPEN))\
        .connect(start_)
        
        start_.connect(Super('super')).connect(start_)
        start_.connect(Abstract('abstract')).connect(start_)
        start_.connect(Prefix('prefix')).connect(start_)
        start_.connect(Implements('implements')).connect(start_)
        start_.connect(end_)
                
        end_.connect(tnode(BRACE_CLOSE)).connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        nameNode = astNode.getChildById('classname')
        res.addChild(AstNode('name', nameNode.getText()))
        
        self._addOptionalChild(res, astNode, 'super')
        self._addOptionalChild(res, astNode, 'abstract')
        self._addOptionalChild(res, astNode, 'prefix')
        self._addOptionalChild(res, astNode, 'implements')
        
        return res
    
    def _addOptionalChild(self, parent, astNode, ident):
        
        node = astNode.getChildById(ident)
        if node:
            node.setId('')
            parent.addChild(node)
      
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
    
class Prefix(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'prefix', ident)
        
    def expand(self, start, end, context):
        
        start\
        .connect(tnode(PREFIX))\
        .connect(tnode(ID, 'id'))\
        .connect(tnode(SEMICOLON))\
        .connect(end)
        
    def transform(self, astNode):
        
        idNode = astNode.getChildById('id')
        
        return AstNode(self.getName(), idNode.getText())
        
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