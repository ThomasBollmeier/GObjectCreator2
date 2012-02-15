#
# Copyright 2011 Thomas Bollmeier
#
# This file is part of GObjectCreator2.
#
# GObjectCreator2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GObjectCreator2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GObjectCreator2.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from goc_parser import GOCParser

class Reader(object):

    def __init__(self):
        
        self._inclPaths = [os.curdir]
        self._root = None
        
    def addIncludePath(self, path):

        self._inclPaths.append(path)
        
    def readFile(self, fileName):
        
        self._asTrees = {}
        self._createAst(fileName, True)
        
    def walk(self, visitor):
        
        if not self._root:
            raise Exception('No syntax tree has been created')
        
        self._walkGrammar(visitor)
        
    def _walkGrammar(self, visitor):
        
        methods = {
                   'package': self._walkPackage,
                   'gobject': self._walkGObject,
                   'ginterface': self._walkGInterface,
                   'gerror': self._walkGError,
                   'genum': self._walkGEnum,
                   'gflags': self._walkGFlags,
                   'gtype': self._walkGType
                   }
        
        for child in self._root.getChildren():
            try:
                methods[child.getName()](child, visitor)
            except KeyError:
                pass
        
    def _walkPackage(self, package, visitor):
        
        methods = {
                   'package': self._walkPackage,
                   'gobject': self._walkGObject,
                   'ginterface': self._walkGInterface,
                   'gerror': self._walkGError,
                   'genum': self._walkGEnum,
                   'gflags': self._walkGFlags,
                   'gtype': self._walkGType
                   }
        
        name = package.getChild('name').getText()
        
        visitor.package_begin(name, self._isExternal(package))
        
        for child in package.getChildren():
            
            childName = child.getName()
            if childName in methods:
                methods[childName](child, visitor)
                    
        visitor.package_end(name)
    
    def _walkGObject(self, gobject, visitor):
        
        name = gobject.getChild('name').getText()
        
        node = gobject.getChild('super')
        if node:
            super = node.getText()
        else:
            super = ''
        
        interfaces = []
        for node in gobject.getChildrenByName('implements'):
            interfaces.append(node.getText())
        
        attrs = {}
        self._addAttr(attrs, gobject, 'abstract')
        self._addAttr(attrs, gobject, 'final')
        self._addAttr(attrs, gobject, 'prefix')
                
        visitor.gobject_begin(name,
                              super,
                              interfaces,
                              attrs,
                              self._isExternal(gobject)
                              )
        
        methods = {
                   'constructor': self._walkConstructor,
                   'method': self._walkMethod,
                   'override': self._walkOverride,
                   'attribute': self._walkAttribute,
                   'property': self._walkProperty,
                   'signal': self._walkSignal
                   }
        
        for child in gobject.getChildren():
            
            childName = child.getName()
            if childName in methods:
                methods[childName](child, visitor)
            
        visitor.gobject_end(name)
        
    def _walkConstructor(self, constructor, visitor):
        
        propInits = {}
        node = constructor.getChild('initProperties')
        if node:
            for child in node.getChildren():
                propName = child.getChild('name').getText()
                value = child.getChild('value')
                if value:
                    valueName = value.getText()
                    isCode = False
                else:
                    codeValue = child.getChild('codeValue')
                    valueName = codeValue.getChild('enum').getText()
                    valueName += '.' + codeValue.getChild('code').getText()
                    isCode = True
                propInits[propName] = PropInitValue(valueName, isCode)
        
        visitor.constructor_begin(propInits)
        
        for paramInfo in self._getParameters(constructor, isConstructor=True):
            visitor.parameter(paramInfo)
                
        visitor.constructor_end()
        
    def _walkMethod(self, method, visitor):
        
        name = method.getChild('name').getText()
        attrs = {}
        resultNode = method.getChild('result')
        if resultNode:
            typeNode = self._getTypeNode(resultNode)
            resultTypeInfo = typeNode and self._getTypeInfo(typeNode) or None
            modifiers = self._getModifiers(resultNode)
            resultInfo = ParamInfo('', resultTypeInfo, modifiers)
        else:
            resultInfo = None
            
        self._addAttr(attrs, method, 'scope')
        self._addAttr(attrs, method, 'visibility')
        self._addAttr(attrs, method, 'inheritance')
        self._addAttr(attrs, method, 'further_params')
        
        visitor.method_begin(name, attrs, resultInfo)
        
        for paramInfo in self._getParameters(method):
            visitor.parameter(paramInfo)
        
        visitor.method_end(name)
        
    def _walkOverride(self, override, visitor):
        
        visitor.override(override.getText())
        
    def _walkAttribute(self, attribute, visitor):
        
        name = attribute.getChild('name').getText()
        typeInfo = self._getTypeInfo(self._getTypeNode(attribute))
        attrs = {}
        self._addAttr(attrs, attribute, 'scope')
        self._addAttr(attrs, attribute, 'visibility')
        
        visitor.attribute(name, typeInfo, attrs)
        
    def _walkProperty(self, prop, visitor):
        
        name = prop.getChild('name').getText()
        
        attrs = {}
        
        self._addAttr(attrs, prop, 'type')
        self._addAttr(attrs, prop, 'access')
        self._addAttr(attrs, prop, 'description')
        
        gtypeNode = prop.getChild('gtype')
        if gtypeNode:
            if gtypeNode.hasChildren():
                gtypeName = gtypeNode.getChild('typeName').getText()
                nameIsTypeName = True
            else:
                gtypeName = gtypeNode.getText()
                nameIsTypeName = False 
            attrs['gtype'] = GTypeValue(gtypeName, nameIsTypeName)
            
        for childName in ['min', 'max', 'default']:
            child = prop.getChild(childName)
            if child:
                attrs[childName] = self._getPropValue(child)
                
        if prop.getChild('autoCreate'):
            attrs['auto_create'] = True
        
        visitor.property(name, attrs)
        
    def _getPropValue(self, node):
        
        valueNode = node.getChild('value')
        if valueNode:
            value = valueNode.getText()
            valueIsCodename = False
        else:
            codeValueNode = node.getChild('codeValue')
            value = codeValueNode.getChild('enum').getText()
            value += '.' + codeValueNode.getChild('code').getText()
            valueIsCodename = True
            
        return CodeValue(value, valueIsCodename)
    
    def _walkSignal(self, signal, visitor):
        
        name = signal.getChild('name').getText()
        
        resultNode = signal.getChild('result')
        if resultNode:
            typeNode = self._getTypeNode(resultNode)
            resultType = typeNode and self._getTypeInfo(typeNode) or None        
            resultModifiers = self._getModifiers(signal)
        else:
            resultType = None
            resultModifiers = []
            
        parameters = []
        for param in signal.getChildrenByName('parameter'):
            parName = param.getChild('name').getText()
            parType = self._getTypeInfo(self._getTypeNode(param))
            parModifiers = self._getModifiers(param)
            parameters.append((parName, parType, parModifiers))
        
        visitor.signal(name, resultType, resultModifiers, parameters)
    
    def _walkGInterface(self, ginterface, visitor):
        
        name = ginterface.getChild('name').getText()
        attrs = {}
        self._addAttr(attrs, ginterface, 'prefix')
        
        visitor.ginterface_begin(name,
                                 attrs,
                                 self._isExternal(ginterface)
                                 )

        methods = {
                   'method': self._walkMethod,
                   'signal': self._walkSignal
                   }
        
        for child in ginterface.getChildren():
            
            childName = child.getName()
            if childName in methods:
                methods[childName](child, visitor)
        
        visitor.ginterface_end(name)
        
    def _walkGError(self, gerror, visitor):
        
        name = gerror.getChild('name').getText()
        codes = [child.getText() for child in gerror.getChildrenByName('code')]
        
        visitor.error_domain(name, codes, self._isExternal(gerror))
    
    def _walkGEnum(self, genum, visitor):
        
        name = genum.getChild('name').getText()
        
        codeValues = []
        for child in genum.getChildrenByName('code'):
            if not child.hasChildren():
                code = child.getText()
                value = None
            else:
                code = child.getChild('name').getText()
                value = child.getChild('value').getText()
            codeValues.append((code, value))
        
        visitor.enumeration(name, codeValues, self._isExternal(genum))
            
    def _walkGFlags(self, gflags, visitor):
        
        name = gflags.getChild('name').getText()
        codes = [child.getText() for child in gflags.getChildrenByName('code')]
        
        visitor.flags(name, codes, self._isExternal(gflags))
    
    def _walkGType(self, gtype, visitor):
        
        visitor.gtype(gtype.getText(), self._isExternal(gtype))
              
    def _createAst(self, fileName, isMainGOCFile):
        
        filePath = ''
        for inclPath in self._inclPaths:
            path = inclPath + os.sep + fileName
            path = os.path.abspath(path)
            if os.path.exists(path):
                filePath = path
                break
            
        if not filePath:
            raise Exception("File '%s' could not be found" % fileName)
        
        if filePath in self._asTrees:
            # File has already been processed:
            return self._asTrees[filePath]
        
        res = GOCParser().parseFile(filePath)
        if isMainGOCFile:
            self._root = res

        self._resolveIncludes(res, isMainGOCFile)
        
        self._asTrees[filePath] = res
        
        return res
        
    def _resolveIncludes(self, root, isMainRoot):
        
        tmp = []
        
        for child in root.getChildren():
            
            if not child.getName() == 'include':
                child.external = not isMainRoot
                tmp.append(child)
            else:
                fileName = child.getChild('file').getText()
                ast = self._createAst(fileName, False)
                for child2 in ast.getChildren():
                    child2.external = True
                    tmp.append(child2)
        
        root.removeChildren()        
        for child in tmp:
            root.addChild(child)
            
    def _isExternal(self, node):
        
        curNode = node
        while curNode and ( not curNode is self._root ):
            try:
                return curNode.external
            except AttributeError:
                pass
            curNode = curNode.getParent()
            
        return False
    
    def _addAttr(self, attrs, objNode, attrName, childName=''):
        
        child = objNode.getChild(childName or attrName)
        if child:
            attrs[attrName] = child.getText() or True
            
    def _getParameters(self, method, isConstructor=False):
        
        res = []
        
        for param in method.getChildrenByName('parameter'):
            name = param.getChild('name').getText()
            typeInfo = self._getTypeInfo(self._getTypeNode(param))
            modifiers = self._getModifiers(param)
            if not isConstructor:
                res.append(ParamInfo(name, typeInfo, modifiers))
            else:
                node = param.getChild('bindProperty')
                bindTo = node and node.getText() or ''
                res.append(ConstructorParamInfo(name, typeInfo, modifiers, bindTo))
                    
        return res
    
    def _getModifiers(self, node):
        
        res = []
        if node.getChild('const'):
            res.append('const')
            
        return res
    
    def _getTypeNode(self, node):
        
        for name in ['type', 'reference', 'list']:
            typeNode = node.getChild(name)
            if typeNode:
                return typeNode
            
        return None
    
    def _getTypeInfo(self, typeNode):
        
        name = typeNode.getName()
        
        if name == 'type':
            return TypeInfo(typeNode.getText())
        elif name == 'reference':
            node = typeNode.getChildren()[0]
            refType = self._getTypeInfo(node)
            return RefTypeInfo(refType)
        elif name == 'list':
            node = typeNode.getChildren()[0]
            lineType = self._getTypeInfo(node)
            return ListTypeInfo(lineType)
        else:
            raise Exception('Cannot determine type info')
            
class TypeInfo(object):

    def __init__(self, name):

        self._name = name

    def get_name(self):

        return self._name

class RefTypeInfo(TypeInfo):

    def __init__(self, ref_type):

        TypeInfo.__init__(self, "")
        self._ref_type = ref_type

    def get_name(self):

        return "%s*" % self._ref_type.get_name()

    def get_ref_type(self):

        return self._ref_type

class ListTypeInfo(TypeInfo):

    def __init__(self, line_type):

        TypeInfo.__init__(self, "")
        self._line_type = line_type

    def get_name(self):

        return "%s[]" % self._line_type.get_name()

    def get_line_type(self):

        return self._line_type

class ParamInfo(object):

    def __init__(self, name, type_info, modifiers):

        self.name = name
        self.type_info = type_info
        self.modifiers = modifiers

class ConstructorParamInfo(ParamInfo):

    def __init__(self, name, type_info, modifiers, bind_to):

        ParamInfo.__init__(self, name, type_info, modifiers)
        self.bind_to = bind_to

class GTypeValue(object):

    def __init__(self, name, is_typename=False):

        self.name = name
        self.is_typename = is_typename

class PropInitValue(object):

    def __init__(self, name, is_codename=False):

        self.name = name
        self.is_codename = is_codename
        
CodeValue = PropInitValue

class GOCVisitor(object):

    def __init__(self):

        pass

    def package_begin(self, name, is_external):

        pass

    def package_end(self, name):

        pass

    def gobject_begin(self,
                      name,
                      super,
                      interfaces,
                      attrs,
                      is_external
                      ):

        pass

    def gobject_end(self, name):

        pass

    def ginterface_begin(self, name, attrs, is_external):

        pass

    def ginterface_end(self, name):

        pass

    def gtype(self, name, is_external):

        pass

    def error_domain(self, name, codes, is_external):

        pass

    def enumeration(self, name, codevals, is_external):

        pass

    def flags(self, name, codes, is_external):

        pass

    def method_begin(self,
                     name,
                     attrs,
                     result_info
                    ):

        pass

    def method_end(self, name):

        pass

    def constructor_begin(self, prop_inits):

        pass

    def constructor_end(self):

        pass

    def signal(self, name, result_type, result_modifiers, args):

        pass

    def override(self, name):

        pass

    def parameter(self, parameter_info):

        pass

    def attribute(self,
                  name,
                  type_info,
                  attrs):

        pass

    def property(self,
                 name,
                 attrs):

        pass
