#! coding=UTF-8

from tbparser.grammar import Rule, tokenNode as tnode, sequence, zeroToOne, zeroToMany
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import ID, NAMESPACE_SEP, NAMESPACE_ROOT_SEP, \
UNSIGNED, INTEGER, LONG, NULL, BOOLEAN, BYTE, STRING, FLOAT, DOUBLE, POINTER

class TypeName(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'typeName', ident)
        
    def expand(self, start, end, context):
        
        start.connect(TypePath('user-defined')).connect(end)
        start.connect(zeroToOne(tnode(UNSIGNED, 'unsigned'))).connect(tnode(INTEGER,'integer')).connect(end)
        start.connect(zeroToOne(tnode(UNSIGNED, 'unsigned'))).connect(tnode(LONG,'long')).connect(end)
        start.connect(tnode(NULL, 'null')).connect(end)
        start.connect(tnode(BOOLEAN, 'boolean')).connect(end)
        start.connect(tnode(BYTE, 'byte')).connect(end)
        start.connect(tnode(STRING, 'string')).connect(end)
        start.connect(tnode(FLOAT, 'float')).connect(end)
        start.connect(tnode(DOUBLE, 'double')).connect(end)
        start.connect(tnode(POINTER, 'pointer')).connect(end)
        
    def transform(self, astNode):
        
        identifiers = {'user-defined': lambda node: node.getText(),
                       'integer': lambda node: self._get_int_or_long(node, astNode),
                       'long': lambda node: self._get_int_or_long(node, astNode),
                       'null': lambda node: node.getText(),
                       'boolean': lambda node: node.getText(),
                       'byte': lambda node: node.getText(),
                       'string': lambda node: node.getText(),
                       'float': lambda node: node.getText(),
                       'double': lambda node: node.getText(),
                       'pointer': lambda node: node.getText()
                       }
         
        typeName = ''
        for ident in identifiers: 
            node = astNode.getChildById(ident)
            if node:
                typeName = identifiers[ident](node)
                break
            
        return AstNode(self.getName(), typeName)
        
    def _get_int_or_long(self, node, parent):
        
        unsignedNode = parent.getChildById('unsigned')
        if not unsignedNode:
            return node.getText()
        else:
            return 'unsigned %s' % node.getText()
       
class TypePath(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'typePath', ident)
        
    def expand(self, start, end, context):
        
        seq = sequence(tnode(ID), tnode(NAMESPACE_SEP))
        
        start\
        .connect(zeroToOne(tnode(NAMESPACE_ROOT_SEP)))\
        .connect(zeroToMany(seq))\
        .connect(tnode(ID))\
        .connect(end)
        
    def transform(self, astNode):
        
        typePath = ""
        for child in astNode.getChildren():
            typePath += child.getText()
            
        return AstNode(self.getName(), typePath)