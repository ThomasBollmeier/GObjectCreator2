#! coding=UTF-8
from tbparser.grammar import Rule, tokenNode as tnode, sequence, zeroToMany, fork, \
defineRule, expand, transform, connector
from tbparser.parser import AstNode
from gobjcreator2.input.grammar.tokens import *
from gobjcreator2.input.grammar.type_name import TypeName, TypePath

class ComposedId(Rule):
    
    def __init__(self, ident=''):
        
        Rule.__init__(self, 'composedId', ident)
        
    def expand(self, start, end, context):
        
        seq = sequence(tnode(DASH), tnode(ID))
        start\
        .connect(tnode(ID))\
        .connect(zeroToMany(seq))\
        .connect(end)
        
    def transform(self, astNode):
        
        text = ''
        for child in astNode.getChildren():
            text += child.getText()
            
        return AstNode(self.getName(), text)
    
class EnumRule(Rule):
    
    def __init__(self, name, enumTokenType, valueTokenTypes, ident):
        
        Rule.__init__(self, name, ident)
        
        self._enumTokenType = enumTokenType
        self._valueTokenTypes = valueTokenTypes
        
    def expand(self, start, end, context):    
        
        values = []
        for vtt in self._valueTokenTypes:
            values.append(tnode(vtt, 'value'))
        
        start\
        .connect(tnode(self._enumTokenType))\
        .connect(tnode(COLON))\
        .connect(fork(*values))\
        .connect(tnode(SEMICOLON))\
        .connect(end)    
        
    def transform(self, astNode):
        
        return AstNode(self.getName(), astNode.getChildById('value').getText())
        
class Visibility(EnumRule):
    
    def __init__(self, ident=''):
        
        values = [PUBLIC, PROTECTED, PRIVATE]
        EnumRule.__init__(self, 'visibility', VISI, values, ident)
        
class Inheritance(EnumRule):
    
    def __init__(self, ident=''):
        
        values = [FINAL, VIRTUAL, ABSTRACT]
        EnumRule.__init__(self, 'inheritance', INHERITANCE, values, ident)
        
class Scope(EnumRule):
    
    def __init__(self, ident=''):
        
        values = [INSTANCE, STATIC]
        EnumRule.__init__(self, 'scope', SCOPE, values, ident)
        
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
        
ArgType = defineRule('argType')

@expand(ArgType)
def argtype_expand(start, end, context):
    
    start.connect(TypeName('type')).connect(end)
    
    start\
    .connect(tnode(REF, 'reference'))\
    .connect(tnode(PAR_OPEN))\
    .connect(ArgType('arg'))\
    .connect(tnode(PAR_CLOSE))\
    .connect(end)
    
    start\
    .connect(tnode(LIST, 'list'))\
    .connect(tnode(PAR_OPEN))\
    .connect(ArgType('arg'))\
    .connect(tnode(PAR_CLOSE))\
    .connect(end)
        
@transform(ArgType)
def argtype_transform(astNode):
    
    for ident in ['type', 'reference', 'list']:
        
        node = astNode.getChildById(ident)
        if not node:
            continue
        node.setId('')
        
        if ident == 'type':
            return AstNode('type', node.getText())
        else:
            res = AstNode(ident)
            argNode = astNode.getChildById('arg')
            argNode.setId('')
            res.addChild(argNode)
            return res

    raise Exception('AST transformation failed')
            
Type = defineRule('type')
        
@expand(Type)
def type_expand(start, end, context):
    
    start\
    .connect(tnode(TYPE))\
    .connect(tnode(COLON))\
    .connect(ArgType('type'))\
    .connect(tnode(SEMICOLON))\
    .connect(end)
    
@transform(Type)
def type_transform(astNode):
    
    return astNode.getChildById('type')

LiteralOrCode = defineRule('literalOrCode')

@expand(LiteralOrCode)
def _lc_expand(start, end, context):
    
    start\
    .connect(tnode(LITERAL, 'value'))\
    .connect(end)
    
    start\
    .connect(TypePath('enum'))\
    .connect(tnode(DOT))\
    .connect(tnode(ID, 'code'))\
    .connect(end)

@transform(LiteralOrCode)
def _lc_transform(astNode):
    
    valueNode = astNode.getChildById('value')
    if valueNode:
        text = valueNode.getText()
        text = text[1:-1]
        return AstNode('value', text)
        
    enumNode = astNode.getChildById('enum')
    if enumNode:
        res = AstNode('codeValue')
        res.addChild(AstNode('enum', enumNode.getText()))
        codeNode = astNode.getChildById('code')
        res.addChild(AstNode('code', codeNode.getText()))
        return res
    
    raise Exception('Literal or code cannot be transformed')

Code = defineRule('code')

@expand(Code)
def _code_expand(start, end, context):
    
    start_ = connector()
    
    start\
    .connect(tnode(CODE))\
    .connect(tnode(ID, 'name'))\
    .connect(start_)
    
    start_.connect(tnode(SEMICOLON)).connect(end)
    
    if context.getEnvVar('ENUMERATION'):
        
        start_\
        .connect(tnode(BRACE_OPEN))\
        .connect(tnode(VALUE))\
        .connect(tnode(COLON))\
        .connect(tnode(INT, 'value'))\
        .connect(tnode(SEMICOLON))\
        .connect(tnode(BRACE_CLOSE))\
        .connect(end)

@transform(Code)
def _code_transform(astNode):
    
    nameNode = astNode.getChildById('name')
    valNode = astNode.getChildById('value')
    
    if not valNode:
        res = AstNode('code', nameNode.getText())
    else:
        res = AstNode('code')
        res.addChild(AstNode('name', nameNode.getText()))
        res.addChild(AstNode('value', valNode.getText()))
    
    return res