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


import antlr3
from gobjcreator2.input.GOCLexer import GOCLexer
from gobjcreator2.input.GOCParser import *
from gobjcreator2.input.goc_tree_adaptor import GOCTreeAdaptor
import os

class Reader(object):

    def __init__(self):

        self._walk_method = {
            PACKAGE: self._walk_package,
            GOBJECT: self._walk_gobject,
            GINTERFACE: self._walk_ginterface,
            GTYPE: self._walk_gtype,
            ERROR_DOMAIN: self._walk_error_domain,
            ENUMERATION: self._walk_enumeration,
            FLAGS: self._walk_flags,
            METHOD: self._walk_method,
            CONSTRUCTOR: self._walk_constructor,
            OVERRIDE: self._walk_override,
            ATTRIBUTE: self._walk_attribute,
            PROPERTY: self._walk_property,
            SIGNAL: self._walk_signal
        }

        self._adaptor = GOCTreeAdaptor()
        self._root_node = None
        self._include_paths = [os.curdir]
        self._main_goc_file = ""

    def add_include_path(self, path):

        self._include_paths.append(path)

    def read_file(self, file_path):

        self._syntax_tree = {}
        self._root_node = self._create_ast_from_file(file_path)
        
    def set_main_goc_file(self, path):
        
        self._main_goc_file = os.path.abspath(path)

    def walk_syntax_tree(self, visitor):

        if self._root_node is None:
            return

        for child in self._root_node.getChildren():
            self._walk(child, visitor)
            
    def _is_external(self, node):
        
        return os.path.normpath(node.goc_file_path) != \
            os.path.normpath(self._main_goc_file)
            
    def _create_ast_from_file(self, filename):
        """
        read file and return abstract syntax tree (AST)
        """
        for path in self._include_paths:
            file_path = path + os.sep + filename
            file_path = os.path.abspath(file_path)
            if os.path.exists(file_path):
                break
            else:
                file_path = ""
                continue
            
        if file_path in self._syntax_tree:
            return self._syntax_tree[file_path]

        stream = antlr3.ANTLRFileStream(file_path)
        lexer = GOCLexer(stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = GOCParser(tokens)
        parser.adaptor = self._adaptor

        # Set path of currently processed file to separate
        # external(=included) model parts from the parts in the main file:
        self._adaptor.set_goc_file_path(file_path)
        res = parser.defFile().tree
        self._adaptor.set_goc_file_path("")
                
        self._syntax_tree[file_path] = res
        self._resolve_includes(res)

        return res

    def _resolve_includes(self, tree):

        top_nodes = tree.getChildren()

        for top_node in top_nodes:

            if top_node.getType() == INCLUDE:
                filename = top_node.getChildren()[0].getText().strip('"')
                if not filename in self._syntax_tree:
                    included_tree = self._create_ast_from_file(filename)
                    new_tree = self._adaptor.nil()
                    for child in included_tree.getChildren():
                        new_tree.addChild(child)
                    index = top_node.getChildIndex()
                    tree.replaceChildren(index, index, new_tree)
                else:
                    # include has already been resolved
                    tree.deleteChild(top_node.getChildIndex())

    def _walk(self, node, visitor):
        
        type = node.getType()

        try:
            method = self._walk_method[type]
            method(node, visitor)
        except KeyError:
            for child in node.getChildren():
                self._walk(child, visitor)

    def _walk_package(self, node, visitor):

        children = node.getChildren()
        name = children[0].getText()

        visitor.package_begin(name, self._is_external(node))

        for child in children[1:]:
            self._walk(child, visitor)
        
        visitor.package_end(name)

    def _walk_gobject(self, node, visitor):

        children = node.getChildren()
        name = children[0].getText()
        super = ""
        interfaces = []
        attrs = {}
        other_children = []
        for child in children[1:]:
            type  = child.getType()
            if type == SUPER:
                super = self._get_type_name(child.children[0])
            elif type == IMPLEMENTS:
                interfaces.append(self._get_type_name(child.children[0]))
            elif type == ABSTRACT:
                attrs["abstract"] = True
            elif type == PREFIX:
                attrs["prefix"] = child.getChildren()[0].getText()
            else:
                other_children.append(child)
        
        visitor.gobject_begin(name, super, interfaces, 
                              attrs, self._is_external(node))

        for child in other_children:
            self._walk(child, visitor)

        visitor.gobject_end(name)

    def _walk_ginterface(self, node, visitor):

        children = node.getChildren()
        name = children[0].getText()
        attrs = {}
        other_children = []

        for child in children[1:]:
            type = child.getType()
            if type == PREFIX:
                attrs["prefix"] = child.getChildren()[0].getText()
            else:
                other_children.append(child)

        visitor.ginterface_begin(name, attrs, self._is_external(node))

        for child in other_children:
            self._walk(child, visitor)

        visitor.ginterface_end(name)

    def _walk_gtype(self, node, visitor):

        name = node.getChildren()[0].getText()

        visitor.gtype(name, self._is_external(node))

    def _walk_error_domain(self, node, visitor):

        name = node.getChildren()[0].getText()
        codes = []
        for child in node.getChildren()[1:]:
            codes.append(child.getText())

        visitor.error_domain(name, codes, self._is_external(node))

    def _walk_enumeration(self, node, visitor):

        name = node.getChildren()[0].getText()
        codevals = []
        for child in node.getChildren()[1:]:
            children = child.getChildren()
            code = children[0].getText()
            try:
                value = children[1].getText()
            except IndexError:
                value = None
            codevals.append((code, value))

        visitor.enumeration(name, codevals, self._is_external(node))

    def _walk_flags(self, node, visitor):

        name = node.getChildren()[0].getText()
        codes = []
        for child in node.getChildren()[1:]:
            codes.append(child.getText())

        visitor.flags(name, codes, self._is_external(node))

    def _walk_method(self, node, visitor):

        name = node.getChildren()[0].getText()
        attrs = {}
        result_info = None
        parameters = []

        for child in node.getChildren()[1:]:
            type = child.getType()
            if type == VISIBILITY:
                attrs["visibility"] = child.getChildren()[0].getText()
            elif type == SCOPE:
                attrs["scope"] = child.getChildren()[0].getText()
            elif type == INHERITANCE:
                attrs["inheritance"] = child.getChildren()[0].getText()
            elif type == RESULT:
                result_type_node = child.getChildren()[0]
                result_type_info = self._get_type_info(result_type_node)
                try:
                    modifiers_node = child.getChildren()[1]
                    modifiers = self._get_modifiers(modifiers_node)
                except IndexError:
                    modifiers = []
                result_info = ParamInfo("", result_type_info, modifiers)
            elif type == PARAMETER:
                param_name = child.getChildren()[0].getText()
                param_type_info = self._get_type_info(child.getChildren()[1])
                try:
                    modifiers = self._get_modifiers(child.getChildren()[2])
                except IndexError:
                    modifiers = []
                parameters.append(ParamInfo(param_name, param_type_info, modifiers))

        visitor.method_begin(name, attrs, result_info)

        for param_info in parameters:
            visitor.parameter(param_info)

        visitor.method_end(name)

    def _walk_constructor(self, node, visitor):

        parameters = []
        prop_inits = {}

        for child in node.getChildren():
            type = child.getType()
            if type == PARAMETER:
                param_name = child.getChildren()[0].getText()
                param_type_info = self._get_type_info(child.getChildren()[1])
                modifiers = []
                bind_to = ""
                try:
                    for node in child.getChildren()[2:]:
                        if node.getType() == MODIFIERS:
                            modifiers = self._get_modifiers(node)
                        elif node.getType() == BIND_PROPERTY:
                            bind_to = node.getChildren()[0].getText()
                except IndexError:
                    pass
                parameters.append(ConstructorParamInfo(
                        param_name, param_type_info, modifiers, bind_to
                        ))
            elif type == INIT_PROPERTIES:
                props = child.getChildren()
                for prop in props:
                    name = prop.getChildren()[0].getText()
                    args = prop.getChildren()[1:]
                    if len(args) == 1:
                        value_name = args[0].getText()
                        is_code = False
                    else:
                        value_name = self._get_type_name(args[0])
                        value_name += "." + args[1].getText()
                        is_code = True
                    prop_inits[name] = PropInitValue(value_name, is_code)
                    
        visitor.constructor_begin(prop_inits)

        for param_info in parameters:
            visitor.parameter(param_info)

        visitor.constructor_end()

    def _walk_signal(self, node, visitor):

        children = node.getChildren()

        signal_parts = children[0].getChildren()
        name = ""
        for signal_part in signal_parts:
            if name:
                name += "-"
            name += signal_part.getText()
        result_type = None
        args = []

        for child in children[1:]:
            type = child.getType()
            if type == RESULT:
                result_type = self._get_type_info(child.getChildren()[0])
            elif type == PARAMETER:
                arg_name = child.getChildren()[0].getText()
                arg_type = self._get_type_info(child.getChildren()[1])
                args.append((arg_name, arg_type))

        visitor.signal(name, result_type, args)

    def _walk_override(self, node, visitor):

        method_name = node.getChildren()[0].getText()

        visitor.override(method_name)

    def _walk_attribute(self, node, visitor):

        children = node.getChildren()
        name = children[0].getText()
        type_info = self._get_type_info(children[1])
        attrs = {}

        for child in children[2:]:
            token_type = child.getType()
            if token_type == SCOPE:
                attrs["scope"] = child.getChildren()[0].getText()
            elif token_type == VISIBILITY:
                attrs["visibility"] = child.getChildren()[0].getText()

        visitor.attribute(name, type_info, attrs)

    def _walk_property(self, node, visitor):

        children = node.getChildren()
        name = children[0].getText()
        attrs = {}

        for child in children[1:]:
            token_type = child.getType()
            if token_type == PROP_TYPE:
                attrs["type"] = child.getChildren()[0].getText()
            elif token_type == PROP_GTYPE:
                arg = child.getChildren()[0]
                if not arg.getType() == GTYPENAME:
                    type_value = GTypeValue(arg.getText())
                else:
                    type_name = self._get_type_name(arg.getChildren()[0])
                    is_typename = True
                    type_value = GTypeValue(type_name, is_typename)
                attrs["gtype"] = type_value
            elif token_type == PROP_ACCESS:
                attrs["access"] = child.getChildren()[0].getText()
            elif token_type == PROP_DESC:
                attrs["description"] = child.getChildren()[0].getText()
            elif token_type == PROP_MIN:
                attrs["min"] = self._get_prop_value(child)
            elif token_type == PROP_MAX:
                attrs["max"] = self._get_prop_value(child)
            elif token_type == PROP_DEFAULT:
                attrs["default"] = self._get_prop_value(child)
            elif token_type == AUTO_CREATE:
                attrs["auto_create"] = True

        visitor.property(name, attrs)

    def _get_type_info(self, type_arg_node):

        token_type = type_arg_node.getType()
        if token_type == TYPE_NAME:
            return TypeInfo(self._get_type_name(type_arg_node))
        elif token_type == REF_TO:
            ref_type_node = type_arg_node.getChildren()[0]
            return RefTypeInfo(self._get_type_info(ref_type_node))
        elif token_type == LIST_OF:
            line_type_node = type_arg_node.getChildren()[0]
            return ListTypeInfo(self._get_type_info(line_type_node))
        else:
            return None
        
    def _get_type_name(self, type_node):

        res = ""
        for child in type_node.getChildren():
            res += child.getText()

        return res
    
    def _get_prop_value(self, prop_value_node):
        
        children = prop_value_node.getChildren()
        
        if len(children) == 1: # string literal
            value = children[0].getText()
            if value[0] == '"':
                value = value[1:]
            if value[-1] == '"':
                value = value[:-1]
            is_codename = False
        else:
            value = self._get_type_name(children[0]) + "." + children[1].getText()
            is_codename = True
            
        return CodeValue(value, is_codename)
            
    def _get_modifiers(self, modifiers_node):

        res = []
        for child in modifiers_node.getChildren():
            res.append(child.getText())

        return res

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

    def signal(self, name, result_type, args):

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
