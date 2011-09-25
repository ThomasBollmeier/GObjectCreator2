#! coding=UTF-8

from tbparser.grammar import defineRule, expand, transform, \
tokenNode as tnode, connector, zeroToOne
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.type_name import TypeName
from gobjcreator2.input.grammar.misc_rules import Type, Visibility, Scope

Attribute = defineRule('attribute')

@expand(Attribute)
def _expand(start, end, contex):
    
    start_ = connector()
    
    start\
    .connect(tnode(ATTRIBUTE))\
    .connect(tnode(ID, 'name'))\
    .connect(tnode(BRACE_OPEN))\
    .connect(Type('type'))\
    .connect(start_)
    
    start_.connect(Visibility('visi')).connect(start_)
    start_.connect(Scope('scope')).connect(start_)
    
    start_.connect(tnode(BRACE_CLOSE)).connect(end)

@transform(Attribute)
def _transform(astNode):
    
    res = AstNode('attribute')
    
    res.addChild(AstNode('name', astNode.getChildById('name').getText()))
    
    node = astNode.getChildById('type')
    node.setId('')
    res.addChild(node)
    
    node = astNode.getChildById('visi')
    if node:
        node.setId('')
        res.addChild(node)

    node = astNode.getChildById('scope')
    if node:
        node.setId('')
        res.addChild(node)
        
    return res
