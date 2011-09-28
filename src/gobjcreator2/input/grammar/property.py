#! coding=UTF-8

from tbparser.grammar import defineRule, expand, transform, connector,\
tokenNode as tnode, Rule, sequence, Switch
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.misc_rules import ComposedId, EnumRule, LiteralOrCode
from gobjcreator2.input.grammar.type_name import TypeName
import gobjcreator2.input.grammar.util as util

Property = defineRule('property')

@expand(Property)
def prop_expand(start, end, context):
    
    start_ = connector()
    end_ = connector()
    
    start\
    .connect(tnode(PROPERTY))\
    .connect(ComposedId('name'))\
    .connect(tnode(BRACE_OPEN))\
    .connect(start_)
    
    descr = sequence(
                     tnode(DESCRIPTION),
                     tnode(COLON),
                     tnode(LITERAL, 'description'),
                     tnode(SEMICOLON)
                     )
    
    auto = sequence(tnode(AUTO_CREATE, 'auto'), tnode(SEMICOLON))
    
    switch = Switch({
                     TYPE: _PropType('type'),
                     ACCESS: _Access('access'),
                     DESCRIPTION: descr,
                     GTYPE: _PropGType('gtype'),
                     PROP_MAX: _PropMax('max'),
                     PROP_MIN: _PropMin('min'),
                     PROP_DEFAULT: _PropDefault('default'),
                     AUTO_CREATE: auto
                     })
    
    start_.connect(switch).connect(start_)
    start_.connect(end_)
        
    end_.connect(tnode(BRACE_CLOSE)).connect(end)

@transform(Property)
def prop_transform(astNode):
    
    res = AstNode(Property.name)
    
    node = astNode.getChildById('name')
    res.addChild(AstNode('name', node.getText()))
    
    util.addOptionalChild(astNode, res, 'type')
    
    util.addOptionalChild(astNode, res, 'access')
    
    node = astNode.getChildById('description')
    if node:
        text = node.getText()[1:-1]
        res.addChild(AstNode('description', text))
        
    util.addOptionalChild(astNode, res, 'gtype')
    
    util.addOptionalChild(astNode, res, 'max')
    util.addOptionalChild(astNode, res, 'min')
    util.addOptionalChild(astNode, res, 'default')
    
    node = astNode.getChildById('auto')
    if node:
        res.addChild(AstNode('autoCreate'))
    
    return res

class _PropType(EnumRule):
    
    def __init__(self, ident=''):
        
        values = [BOOLEAN,
                  INTEGER,
                  FLOAT,
                  DOUBLE,
                  STRING,
                  POINTER,
                  PROP_TYPE_OBJECT,
                  PROP_TYPE_ENUMERATION
                  ]
        
        EnumRule.__init__(self, 'type', TYPE, values, ident)

_Access = defineRule('access')

@expand(_Access)
def _access_expand(start, end, context):
    
    start_ = connector()
    end_ = connector()
    start.connect(tnode(ACCESS)).connect(tnode(COLON)).connect(start_)
    
    start_.connect(_ReadOnly('val')).connect(end_)
    start_.connect(_InitWrite('val')).connect(end_)
    start_.connect(_ReadWrite('val')).connect(end_)
    
    end_.connect(tnode(SEMICOLON)).connect(end)
    
@transform(_Access)
def _access_transform(astNode):
    
    value = astNode.getChildById('val')
    text = ""
    for node in value.getChildren():
        text += node.getText()
    
    return AstNode(_Access.name, text)
        
_ReadOnly = defineRule('readOnly')

@expand(_ReadOnly)
def _ro_expand(start, end, context):
    
    start\
    .connect(tnode(READ))\
    .connect(tnode(DASH))\
    .connect(tnode(ONLY))\
    .connect(end)

_InitWrite = defineRule('initialWrite')

@expand(_InitWrite)
def _iw_expand(start, end, context):
    
    start\
    .connect(tnode(INITIAL))\
    .connect(tnode(DASH))\
    .connect(tnode(WRITE))\
    .connect(end)

_ReadWrite = defineRule('readWrite')

@expand(_ReadWrite)
def _rw_expand(start, end, context):
    
    start\
    .connect(tnode(READ))\
    .connect(tnode(DASH))\
    .connect(tnode(WRITE))\
    .connect(end)    
    
_PropGType = defineRule('gtype')

@expand(_PropGType)
def _gt_expand(start, end, context):
    
    start_ = connector()
    end_ = connector()
    
    start\
    .connect(tnode(GTYPE))\
    .connect(tnode(COLON))\
    .connect(start_)
    
    start_\
    .connect(tnode(GTYPENAME))\
    .connect(tnode(PAR_OPEN))\
    .connect(TypeName('typeName'))\
    .connect(tnode(PAR_CLOSE))\
    .connect(end_)
    start_.connect(tnode(ID, 'id')).connect(end_)
    
    end_.connect(tnode(SEMICOLON)).connect(end)
    
@transform(_PropGType)
def _gt_transform(astNode):
    
    node = astNode.getChildById('id')
    if node:
        res = AstNode(_PropGType.name, node.getText())
    else:
        node = astNode.getChildById('typeName')
        res = AstNode(_PropGType.name)
        node.setId('')
        res.addChild(node)
        
    return res

class _ValueAssignment(Rule):
    
    def __init__(self, name, keyToken, ident):
        
        Rule.__init__(self, name, ident)
        
        self._keyToken = keyToken
        
    def expand(self, start, end, context):
        
        start\
        .connect(tnode(self._keyToken))\
        .connect(tnode(COLON))\
        .connect(LiteralOrCode('value'))\
        .connect(tnode(SEMICOLON))\
        .connect(end)
        
    def transform(self, astNode):
        
        res = AstNode(self.getName())
        
        util.addChild(astNode, res, 'value')
        
        return res

class _PropMax(_ValueAssignment):
    
    def __init__(self, ident=''):
        
        _ValueAssignment.__init__(self, 'max', PROP_MAX, ident)

class _PropMin(_ValueAssignment):
    
    def __init__(self, ident=''):
        
        _ValueAssignment.__init__(self, 'min', PROP_MIN, ident)
        
class _PropDefault(_ValueAssignment):
    
    def __init__(self, ident=''):
        
        _ValueAssignment.__init__(self, 'default', PROP_DEFAULT, ident)