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


from gobjcreator2.output.writer import ListOut
from gobjcreator2.output.class_intf_writer import ClassIntfWriter
from gobjcreator2.output.func_name_creator import FuncNameCreator
from gobjcreator2.output.marshaller_generator import MarshallerGenerator
import gobjcreator2.output.util as util
from gobjcreator2.metadef.constants import Visibility, Scope
from gobjcreator2.metadef.property import PropAccess, PropType
from gobjcreator2.metadef.method import Method, MethodInheritance
import gobjcreator2.metadef.types as types

class GObjectWriter(ClassIntfWriter):

    def __init__(self, gobject):

        ClassIntfWriter.__init__(self, gobject)
        self._gobj = gobject

        namespace = ""
        package = self._gobj.package
        while package:
            if package.name:
                if namespace:
                    namespace = package.name + "_" + namespace
                else:
                    namespace = package.name + "_"
            package = package.package

        self._vars = {
            "CLASS": self._clifname(self._gobj).upper(),
            "Class": self._clifname(self._gobj),
            "prefix": namespace.lower() + self._base_prefix,
            "NAMESPACE": namespace.upper(),
            "BASENAME": self._basename()
        }
        
        self._func_name_creator = FuncNameCreator()

    def write_header(self):

        self._write_comment()
        self.writeln()

        self.writeln("#ifndef %(CLASS)s_H" % self._vars)
        self.writeln("#define %(CLASS)s_H" % self._vars)
        self.writeln()
        self.writeln('#include "glib-object.h"')
        self.writeln()
        self.writeln("G_BEGIN_DECLS")
        self.writeln()

        if self._gobj.super_class:
            self.writeln('#include "%s_prot.h"' % \
                         self._filename_base(self._gobj.super_class))

        for intf in self._gobj.interfaces:
            self.writeln('#include "%s.h"' % self._filename_base(intf))
        self.writeln()

        self.user_section("header_top", "/* add includes here... */")
        self.writeln()

        if self._gobj.has_attributes(Visibility.PRIVATE, Scope.INSTANCE):
            self.writeln("typedef struct _%(Class)sPriv %(Class)sPriv;" % self._vars)
        if self._gobj.has_attributes(Visibility.PROTECTED, Scope.INSTANCE):
            self.writeln("typedef struct _%(Class)sProt %(Class)sProt;" % self._vars)
        self.writeln()

        self._write_struct()
        
        self._write_class_struct()

        self.writeln("GType %(prefix)s_get_type();" % self._vars)
        self.writeln()

        self._write_init_methods()

        self._write_method_decls(Visibility.PUBLIC)
        
        self._write_properties()

        self._write_macros()

        self.user_section("header_bottom")
        self.writeln()

        self.writeln("G_END_DECLS")
        self.writeln()
        self.writeln("#endif")
        self.writeln()

    def write_header_protected(self):

        self._write_comment()
        self.writeln()

        self.writeln("#ifndef %(CLASS)s_PROT_H" % self._vars)
        self.writeln("#define %(CLASS)s_PROT_H" % self._vars)
        self.writeln()
        self.writeln('#include "glib-object.h"')
        self.writeln()
        self.writeln("G_BEGIN_DECLS")
        self.writeln()
        self.writeln('#include "%s.h"' % self._filename_base(self._gobj))
        self.writeln()
        self.user_section("header_top")
        self.writeln()

        if self._gobj.has_attributes(Visibility.PROTECTED, Scope.INSTANCE):
            self.writeln("struct _%(Class)sProt {" % self._vars)
            self.indent()
            for attr in self._gobj.attributes:
                if attr.visibility != Visibility.PROTECTED or \
                   attr.scope != Scope.INSTANCE:
                    continue
                self.writeln("%s %s;" % \
                             (self.typename(attr.type), attr.name))
            self.unindent()
            self.writeln("};")
            self.writeln()

        self._write_init_methods_prot()

        self.writeln("void")
        self.writeln("%(prefix)s_dispose(GObject* obj);" % self._vars)
        self.writeln()
        self.writeln("void")
        self.writeln("%(prefix)s_finalize(GObject* obj);" % self._vars)
        self.writeln()
        
        self._write_method_decls(Visibility.PROTECTED)

        self.user_section("header_bottom")
        self.writeln()
        self.writeln("G_END_DECLS")
        self.writeln()
        self.writeln("#endif")
        self.writeln()

    def write_source(self):

        self._write_comment()
        self.writeln()

        self.writeln("#include \"%s_prot.h\"" % self._filename_base(self._gobj))
        self.writeln()
        
        default_lines = []
        if self._gobj.signals:
            default_lines.append('#include "%s_marshalller.h"' % \
                                 self._filename_base(self._gobj))
        default_lines.append("/* add further includes ...*/")
        
        self.user_section("source_top", default_lines, indent_level=-1)
        self.writeln()
        
        if self._gobj.has_attributes(Visibility.PRIVATE, Scope.INSTANCE):
            self.writeln("struct _%(Class)sPriv {" % self._vars)
            self.indent()
            for attr in self._gobj.attributes:
                if attr.visibility != Visibility.PRIVATE or \
                   attr.scope != Scope.INSTANCE:
                    continue
                self.writeln("%s %s;" % \
                             (self.typename(attr.type), attr.name))
            self.unindent()
            self.writeln("};")
            self.writeln()
        
        self._write_interface_defs()
        self._write_virtual_defs()    
        self._write_overridden_defs()
        self._write_method_decls(Visibility.PRIVATE, define_as_static=True)
        
        self.user_section("private_methods", "/* define further methods...*/")
        self.writeln()
        
        self._write_property_enum()
        self._write_signals_enum()
        
        self._write_class_init()
        self._write_interfaces_init()
        
        self._write_type_init()
        
        self.writeln("/* ===== implementation ===== */")
        self.writeln()
        
        self._write_instantiation_impl()
        self._write_prop_setter_getter()        
        
        self._write_interface_impls()
        
        self._write_methods_implementation(Visibility.PUBLIC, 
                                           "/* ===== public methods ===== */"
                                           )
        self._write_methods_implementation(Visibility.PROTECTED, 
                                           "/* ===== protected methods ===== */"
                                           )
        self._write_methods_implementation(Visibility.PRIVATE, 
                                           "/* ===== private methods ===== */"
                                           )
        
        self._write_overridden_impls()
        
        self.user_section("source_bottom")
        self.writeln()
                    
    def _write_struct(self):

        self.writeln("typedef struct _%(Class)s {" % self._vars)
        self.indent()
        self.writeln()

        if self._gobj.super_class is None:
            self.writeln("GObject super;")
        else:
            self.writeln("%s super;" % self._clifname(self._gobj.super_class))
        self.writeln()

        has_attrs = False
        for attr in self._gobj.attributes:
            if attr.visibility == Visibility.PUBLIC and \
               attr.scope == Scope.INSTANCE:
                has_attrs = True
                self.writeln("%s %s;" % \
                             (self.typename(attr.type), attr.name)
                             )
        if has_attrs:
            self.writeln()

        self.user_section("public_members",
                          "/* add further public members...*/"
                          )
        self.writeln()

        if self._gobj.has_attributes(Visibility.PROTECTED):
            self.writeln("%(Class)sProt* prot;" % self._vars)
        if self._gobj.has_attributes(Visibility.PRIVATE):
            self.writeln("%(Class)sPriv* priv;" % self._vars)

        self.writeln()
        self.unindent()
        self.writeln("} %(Class)s;" % self._vars)
        self.writeln()

    def _write_properties(self):

        if not self._gobj.properties:
            return

        self.writeln("/* ===== Properties ======")
        for prop in self._gobj.properties:
            descr = prop.description.strip("\"")
            descr = descr.replace('\\"', '"')
            self.write("* %s <-- %s " % (prop.name, descr))
            if prop.access == PropAccess.READ_ONLY:
                self.writeln("(read)")
            elif prop.access == PropAccess.INITIAL_WRITE:
                self.writeln("(read/initial-write)")
            else:
                self.writeln("(read/write)")
        self.writeln("*/")
        self.writeln()
        
    def _write_property_enum(self):
        
        if not self._gobj.properties:
            return
        
        self.writeln("/* ===== properties ===== */")
        self.writeln()
        self.writeln("enum {")
        self.indent()
        first = True
        for prop in self._gobj.properties:
            if first:
                first = False
            else:
                self.writeln(",")
            self.write("PROP_%s" % prop.name.upper())
            if prop is self._gobj.properties[0]:
                self.write(" = 1")
        self.writeln()
        self.unindent()
        self.writeln("};")
        self.writeln()
        self.writeln("static void")
        self.writeln("%(prefix)s_set_property(" % self._vars)
        self.indent()
        self.writeln("GObject* object,")
        self.writeln("guint property_id,")
        self.writeln("const GValue* value,")
        self.writeln("GParamSpec* param_spec")
        self.writeln(");")
        self.unindent()
        self.writeln()
        self.writeln("static void")
        self.writeln("%(prefix)s_get_property(" % self._vars)
        self.indent()
        self.writeln("GObject* object,")
        self.writeln("guint property_id,")
        self.writeln("GValue* value,")
        self.writeln("GParamSpec* param_spec")
        self.writeln(");")
        self.unindent()
        self.writeln()
        
    def _write_property_specs(self):
        
        if not self._gobj.properties:
            return
        
        propspec_write = {
                          PropType.BOOLEAN: self._write_propspec_boolean,
                          PropType.INTEGER: self._write_propspec_integer,
                          PropType.FLOAT: self._write_propspec_float,
                          PropType.DOUBLE: self._write_propspec_double,
                          PropType.STRING: self._write_propspec_string,
                          PropType.POINTER: self._write_propspec_string,
                          PropType.OBJECT: self._write_propspec_object,
                          PropType.ENUMERATION: self._write_propspec_enum
                          }
        
        self.writeln("/* install properties */")
        self.writeln()
        
        for prop in self._gobj.properties:
            
            saved_output = self.output
            list_output = ListOut()
            self.output = list_output
            
            propspec_write[prop.type](prop)
            self.writeln("g_object_class_install_property(")
            self.indent()
            self.writeln("gobj_class,")
            self.writeln("PROP_%s," % prop.name.upper())
            self.writeln("pspec_%s" % prop.name.lower())
            self.writeln(");")
            self.unindent()
            
            self.output = saved_output
            
            self.user_section("property_reg_%s" % prop.name.lower(), 
                              default_code = list_output.get_lines(),
                              indent_level = -1
                              )
            self.writeln()
            
    def _write_propspec_boolean(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_boolean(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        if prop.default is None:
            default = "FALSE"
        else:
            default = self._prop_value_to_string(prop, "default")
        self.writeln(default + ",")
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()
            
    def _write_propspec_integer(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_int(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        if prop.min is None:
            min = "0"
        else:
            min = self._prop_value_to_string(prop, "min")
        self.writeln(min + ",")
        if prop.max is None:
            max = "0"
        else:
            max = self._prop_value_to_string(prop, "max")
        self.writeln(max + ",")
        if prop.default is None:
            default = "0"
        else:
            default = self._prop_value_to_string(prop, "default")
        self.writeln(default + ",")
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()
        
    def _write_propspec_float(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_float(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        if prop.min is None:
            min = "0.0"
        else:
            min = self._prop_value_to_string(prop, "min")
        self.writeln(min + ",")
        if prop.max is None:
            max = "0.0"
        else:
            max = self._prop_value_to_string(prop, "max")
        self.writeln(max + ",")
        if prop.default is None:
            default = "0.0"
        else:
            default = self._prop_value_to_string(prop, "default")
        self.writeln(default + ",")
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()

    def _write_propspec_double(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_double(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        if prop.min is None:
            min = "0.0"
        else:
            min = self._prop_value_to_string(prop, "min")
        self.writeln(min + ",")
        if prop.max is None:
            max = "0.0"
        else:
            max = self._prop_value_to_string(prop, "max")
        self.writeln(max + ",")
        if prop.default is None:
            default = "0.0"
        else:
            default = self._prop_value_to_string(prop, "default")
        self.writeln(default + ",")
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()
    
    def _write_propspec_string(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_string(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        if prop.default is None:
            default = '""'
        else:
            default = '"%s"' % self._prop_value_to_string(prop, "default")
        self.writeln(default + ",")
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()
    
    def _write_propspec_pointer(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_pointer(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()
    
    def _write_propspec_object(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_object(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        if prop.gtype.is_typename:
            gtypename = self.gtypename(prop.gtype.name, self._gobj.package)
        else:
            gtypename = prop.gtype.name
        self.writeln("%s," % gtypename)
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()
    
    def _write_propspec_enum(self, prop):
        
        self.writeln("pspec_%s = g_param_spec_enum(" % prop.name.lower())
        self.indent()
        self._write_propspec_name_descr(prop)
        if prop.gtype.is_typename:
            gtypename = self.gtypename(prop.gtype.name, self._gobj.package)
        else:
            gtypename = prop.gtype.name
        self.writeln("%s," % gtypename)
        if prop.default is None:
            default = "0"
        else:
            default = self._prop_value_to_string(prop, "default")
        self.writeln(default + ",")
        self._write_propspec_flags(prop)
        self.writeln(");")
        self.unindent()
        
    def _write_propspec_name_descr(self, prop):
        
        self.writeln("\"" + prop.name + "\",")
        descr = prop.description.strip("\"")
        self.writeln("\"" + descr + "\",")
        self.writeln("\"" + descr + "\",")
        
    def _write_propspec_flags(self, prop):
        
        if prop.access == PropAccess.READ_ONLY:
            self.writeln("G_PARAM_READABLE|G_PARAM_STATIC_STRINGS")
        elif prop.access == PropAccess.INITIAL_WRITE:
            self.writeln("G_PARAM_READWRITE|G_PARAM_CONSTRUCT_ONLY|G_PARAM_STATIC_STRINGS")
        elif prop.access == PropAccess.READ_WRITE:
            self.writeln("G_PARAM_READWRITE|G_PARAM_STATIC_STRINGS")
            
    def _write_prop_setter_getter(self):
        
        self.writeln("void")
        self.writeln("%(prefix)s_set_property(" % self._vars)
        self.indent()
        self.writeln("GObject* obj,")
        self.writeln("guint property_id,")
        self.writeln("const GValue* value,")
        self.writeln("GParamSpec* param_spec")
        self.writeln(") {")
        self.writeln()
        has_write_props = False
        first = True
        for prop in self._gobj.properties:
            if prop.access == PropAccess.READ_ONLY:
                continue
            if first:
                first = False
                has_write_props = True
                self.write("%s self = " % self.typename(self._gobj))
                self.writeln("%(NAMESPACE)s%(BASENAME)s(obj);" % self._vars)
                self.writeln()
                self.user_section("property_set_data_decls",
                                  "/* data declarations...*/")
                self.writeln()
                self.writeln("switch (property_id) {")
                self.indent()
                self.writeln()
            self.writeln("case PROP_%s:" % prop.name.upper())
            self.indent()
            self._write_prop_set(prop)
            self.unindent()
            self.writeln()
        
        if has_write_props:
            self.writeln("default:")
            self.indent()
            self.writeln("G_OBJECT_WARN_INVALID_PROPERTY_ID(")
            self.indent()
            self.writeln("obj,")
            self.writeln("property_id,")
            self.writeln("param_spec")
            self.writeln(");")
            self.unindent()
            self.unindent()
            self.writeln()
            self.unindent()
            self.writeln("}")
        else:
            self.writeln("G_OBJECT_WARN_INVALID_PROPERTY_ID(")
            self.indent()
            self.writeln("obj,")
            self.writeln("property_id,")
            self.writeln("param_spec")
            self.writeln(");")
            self.unindent()
        
        self.unindent()
        self.writeln()
        self.writeln("}")
        self.writeln()

        self.writeln("void")
        self.writeln("%(prefix)s_get_property(" % self._vars)
        self.indent()
        self.writeln("GObject* obj,")
        self.writeln("guint property_id,")
        self.writeln("GValue* value,")
        self.writeln("GParamSpec* param_spec")
        self.writeln(") {")
        self.writeln()
        has_props = False
        first = True
        for prop in self._gobj.properties:
            if first:
                first = False
                has_props = True
                self.write("%s self = " % self.typename(self._gobj))
                self.writeln("%(NAMESPACE)s%(BASENAME)s(obj);" % self._vars)
                self.writeln()
                self.user_section("property_get_data_decls",
                                  "/* data declarations...*/")
                self.writeln()
                self.writeln("switch (property_id) {")
                self.indent()
                self.writeln()
            self.writeln("case PROP_%s:" % prop.name.upper())
            self.indent()
            self._write_prop_get(prop)
            self.unindent()
            self.writeln()
        
        if has_props:
            self.writeln("default:")
            self.indent()
            self.writeln("G_OBJECT_WARN_INVALID_PROPERTY_ID(")
            self.indent()
            self.writeln("obj,")
            self.writeln("property_id,")
            self.writeln("param_spec")
            self.writeln(");")
            self.unindent()
            self.unindent()
            self.writeln()
            self.unindent()
            self.writeln("}")
        else:
            self.writeln("G_OBJECT_WARN_INVALID_PROPERTY_ID(")
            self.indent()
            self.writeln("obj,")
            self.writeln("property_id,")
            self.writeln("param_spec")
            self.writeln(");")
            self.unindent()
        
        self.unindent()
        self.writeln()
        self.writeln("}")
        self.writeln()
        
    def _write_prop_set(self, prop):
        
        save_out = self.get_output()
        self.set_output(ListOut())
        
        if prop.auto_create:
            if prop.type == PropType.BOOLEAN:
                self.write("self->priv->%s = " % prop.name)
                self.writeln("g_value_get_boolean(value);")
            elif prop.type == PropType.INTEGER:
                self.write("self->priv->%s = " % prop.name)
                self.writeln("g_value_get_integer(value);")
            elif prop.type == PropType.FLOAT:
                self.write("self->priv->%s = " % prop.name)
                self.writeln("g_value_get_float(value);")
            elif prop.type == PropType.DOUBLE:
                self.write("self->priv->%s = " % prop.name)
                self.writeln("g_value_get_double(value);")
            elif prop.type == PropType.STRING:
                self.writeln("if (self->priv->%s" % prop.name + ")")
                self.indent()
                self.writeln("g_free(self->priv->%s);" % prop.name)
                self.unindent()
                self.write("self->priv->%s = " % prop.name)
                self.writeln("g_value_dup_string(value);")
        self.writeln('g_object_notify(obj, "%s");' % prop.name)
        lines = self.get_output().get_lines()
        
        self.set_output(save_out)
        
        self.user_section("property_set_%s" % prop.name, lines,
                          indent_level=-3)
        self.writeln("break;")

    def _write_prop_get(self, prop):
        
        save_out = self.get_output()
        self.set_output(ListOut())
        
        if prop.auto_create:
            if prop.type == PropType.BOOLEAN:
                self.writeln("g_value_set_boolean(value, self->priv->%s);" % prop.name)
            elif prop.type == PropType.INTEGER:
                self.writeln("g_value_set_integer(value, self->priv->%s);" % prop.name)
            elif prop.type == PropType.FLOAT:
                self.writeln("g_value_set_float(value, self->priv->%s);" % prop.name)
            elif prop.type == PropType.DOUBLE:
                self.writeln("g_value_set_double(value, self->priv->%s);" % prop.name)
            elif prop.type == PropType.STRING:
                self.writeln("g_value_set_static_string(value, self->priv->%s);" % prop.name)
        lines = self.get_output().get_lines()
        
        self.set_output(save_out)
        
        self.user_section("property_get_%s" % prop.name, lines,
                          indent_level=-3)
        self.writeln("break;")
            
    def _prop_value_to_string(self, prop, value_name):
        
        value = getattr(prop, value_name)
        if not value.is_codename:
            return value.name
        else:
            return self._code_to_string(value.name)
        
    def _code_to_string(self, code):
        
        enum_name, code_name = code.split(".")
        enum_type = self._gobj.package[enum_name]
        code_name = self.to_underscore(enum_type.name) + "_" + code_name.upper()
        package = enum_type.package
        while package:
            if package.name:
                code_name = package.name.upper() + "_" + code_name
            package = package.package
            
        return code_name
        
    def _write_class_struct(self):

        self.writeln("/* ===== Class ===== */")
        self.writeln()
        self.writeln("typedef struct _%(Class)sClass {" % self._vars)
        self.writeln()
        self.indent()

        if self._gobj.super_class is None:
            self.writeln("GObjectClass super_class;")
        else:
            self.writeln("%sClass super_class;" % \
                         self._clifname(self._gobj.super_class))

        first = True
        for attr in self._gobj.attributes:
            if not attr.scope == Scope.STATIC:
                continue
            if first:
                self.writeln()
                self.writeln("/* == static attributes == */")
                self.writeln()
                first = False
            self.write("%s %s;" % (self.typename(attr.type), attr.name))
            if attr.visibility == Visibility.PUBLIC:
                self.writeln(" /* public */")
            elif attr.visibility == Visibility.PROTECTED:
                self.writeln(" /* protected */")
            elif attr.visibility == Visibility.PRIVATE:
                self.writeln(" /* private */")

        first = True
        for m in self._gobj.methods:
            if m.inheritance_mode == MethodInheritance.FINAL:
                continue
            if first:
                self.writeln()
                self.writeln("/* == virtual methods == */")
                self.writeln()
                first = False
            self._write_method_decl(m, as_pointer=True)

        first = True
        for sig in self._gobj.signals:
            if first:
                self.writeln()
                self.writeln("/* == signals == */")
                self.writeln()
                first = False
            self._write_signal_decl(sig)

        self.unindent()
        self.writeln()
        self.writeln("} %(Class)sClass;" % self._vars)
        self.writeln()
        
    def _write_class_init(self):
        
        self.writeln("/* ===== class initialization ===== */")
        self.writeln()
        self.writeln("static void")
        self.writeln("%(prefix)s_class_init(%(Class)sClass* cls) {" % self._vars)
        self.indent()
        self.writeln()
        
        self.writeln("GObjectClass* gobj_class = G_OBJECT_CLASS(cls);")
        for prop in self._gobj.properties:
            self.writeln("GParamSpec* pspec_%s;" % prop.name.lower())
        self.writeln()
        
        if self._gobj.has_attributes(Visibility.PRIVATE):
            self.writeln("/* Register structure holding private attributes: */")
            self.writeln("g_type_class_add_private (cls, sizeof(%(Class)sPriv));" % self._vars)
            self.writeln()
            
        self.user_section("class_init", "/* init class members ... */")
        self.writeln()
        
        self.writeln("gobj_class->dispose = %(prefix)s_dispose;" % self._vars)
        self.writeln("gobj_class->finalize = %(prefix)s_finalize;" % self._vars)
        self.writeln("gobj_class->set_property = %(prefix)s_set_property;" % self._vars)
        self.writeln("gobj_class->get_property = %(prefix)s_get_property;" % self._vars)
        self.writeln() 
        
        first = True
        for m in self._gobj.methods:
            if m.inheritance_mode != MethodInheritance.VIRTUAL:
                continue
            if first:
                first = False
                self.writeln("/* set default implementations of virtual methods */")
                self.writeln()
            method_name = self._vars["prefix"] + "_" + self._func_name_creator.create_impl_func_name(m.name)
            self.writeln("cls->%s = %s;" % (m.name, method_name))
        if not first:
            self.writeln()
                
        first = True
        for info in self._gobj.overridden_methods:
            if first:
                first = False
                self.writeln("/* set implementations of overridden methods */")
                self.writeln()
            method_name = self._vars["prefix"] + "_" + info.method.name + "_im"
            cast_name = self._clifname(info.defined_in) + "Class"
            self.writeln("(%s* cls)->%s = %s;" % (cast_name, info.method.name, method_name))
        if not first:
            self.writeln()    
            
        self._write_property_specs()
                
        self._write_add_signals()
                      
        self.writeln()
        self.unindent()
        self.writeln("}")
        
        self.writeln()
        
    def _write_interfaces_init(self):
        
        self.writeln("/* ===== interfaces ===== */")
        self.writeln()
        
        for interface in self._gobj.interfaces:
            
            self.writeln("static void")
            
            method_name = "%(prefix)s_" % self._vars
            iface_name = util.camelcase_to_underscore(self._clifname(interface))
            method_name += iface_name.lower() + "_init("
            method_name += self._clifname(interface) + "Iface* iface) {"
            self.writeln(method_name)
            self.indent()
            self.writeln()
            for method in interface.methods:
                line = "iface->%s = " % method.name
                line += "%(prefix)s_" % self._vars
                line += "%s;" % \
                    self._func_name_creator.create_impl_func_name(method.name, 
                                                                  interface.name
                                                                  )
                self.writeln(line)
            self.writeln()
            self.unindent()
            self.writeln("}")
            self.writeln()
        
        self.user_section("external_interfaces_init",
                          "/* Initialize implementation of unmodeled interfaces... */"
                          )
        self.writeln()
        
    def _write_type_init(self):
        
        self.writeln("/* ===== type initialization ==== */")
        self.writeln()
        
        self.writeln("static void")
        self.writeln("%(prefix)s_instance_init(" % self._vars)
        self.indent()
        self.writeln("GTypeInstance* obj,")
        self.writeln("gpointer cls")
        self.writeln(") {")
        self.writeln()
        
        if self._gobj.has_attributes(Visibility.PRIVATE) or \
           self._gobj.has_attributes(Visibility.PROTECTED):
            
            line = "%(Class)s* self = %(NAMESPACE)s%(BASENAME)s(obj);" % self._vars
            self.writeln(line)
            self.writeln()
            
        if self._gobj.has_attributes(Visibility.PRIVATE):
            self.writeln("self->priv = G_TYPE_INSTANCE_GET_PRIVATE(")
            self.indent()
            self.writeln("self,")
            self.writeln("%(NAMESPACE)sTYPE_%(BASENAME)s," % self._vars)
            self.writeln("%(Class)sPriv" % self._vars)
            self.writeln(");")
            self.unindent()
            self.writeln()
            
        if self._gobj.has_attributes(Visibility.PROTECTED):
            self.writeln("self->prot = (%(Class)sProt*) g_new(%(Class)sProt, 1);" % self._vars)
            self.writeln()
            
        lines = []
        lines.append("/* init members, allocate memory, etc ... */")
        lines.append("")
        
        for prop in self._gobj.properties:
            if not prop.auto_create:
                continue
            line = ""
            if prop.type == PropType.BOOLEAN:
                line = "self->priv->%s = FALSE;" % prop.name
            elif prop.type == PropType.INTEGER:
                line = "self->priv->%s = 0;" % prop.name 
            elif prop.type == PropType.FLOAT or prop.type == PropType.DOUBLE:
                line = "self->priv->%s = 0.0;" % prop.name 
            elif prop.type == PropType.STRING:
                line = "self->priv->%s = NULL;" % prop.name
            lines.append(line)
            
        self.user_section("instance_init", 
                          default_code = lines,
                          indent_level = 0
                          )
        self.writeln()
            
        self.unindent()
        self.writeln("}")
        self.writeln()
        
        self._write_get_type_method()
        
    def _write_get_type_method(self):
        
        self.writeln("GType %(prefix)s_get_type() {" % self._vars)
        self.writeln()
        self.indent()
        
        self.writeln("static type_id = 0;")
        self.writeln()
        
        self.writeln("if (type_id == 0) {")
        self.indent()
        self.writeln()
        self.writeln("const GTypeInfo class_info = {")
        self.indent()
        self.writeln("sizeof(%(Class)sClass)," % self._vars)
        self.writeln("NULL, /* base initializer */")
        self.writeln("NULL, /* base finalizer */")
        self.writeln("(GClassInitFunc) %(prefix)s_class_init," % self._vars)
        self.writeln("NULL, /* class finalizer */")
        self.writeln("NULL, /* class data */")
        self.writeln("sizeof(%(Class)s)," % self._vars)
        self.writeln("0,") 
        self.writeln("%(prefix)s_instance_init" % self._vars)
        self.writeln("};")
        self.unindent()
        self.writeln()

        for interface in self._gobj.interfaces:
            ifprefix = util.camelcase_to_underscore(self._clifname(interface)).lower()
            initfunc = "%(prefix)s" % self._vars + "_" + ifprefix + "_init"
            self.writeln("const GInterfaceInfo %s_info = {" % ifprefix)
            self.indent()
            self.writeln("(GInterfaceInitFunc) %s," % initfunc)
            self.writeln("NULL,")
            self.writeln("NULL")
            self.writeln("};")
            self.unindent()
            self.writeln()
            
        self.writeln("type_id = g_type_register_static(")
        self.indent()
        if self._gobj.super_class is None:
            self.writeln("G_TYPE_OBJECT,"),
        else:
            super_basename = util.camelcase_to_underscore(self._gobj.super_class.name).upper()
            self.writeln("%sTYPE_%s," % \
                         (util.namespace_prefix(self._gobj.super_class).upper(),
                          super_basename))
        self.writeln('"%(Class)s",' % self._vars)
        self.writeln("&class_info,")
        if not self._gobj.abstract:
            self.writeln("0")
        else:
            self.writeln("G_TYPE_FLAG_ABSTRACT")
        self.writeln(");")
        self.unindent()
        self.writeln()

        for interface in self._gobj.interfaces:
            
            iftype = util.namespace_prefix(interface).upper()
            iftype += "TYPE_" 
            iftype += util.camelcase_to_underscore(interface.name).upper()
            
            ifprefix = self._clifname(interface)
            ifprefix = util.camelcase_to_underscore(ifprefix)
            ifprefix = ifprefix.lower()
            
            self.writeln("g_type_add_interface_static(")
            self.indent()
            self.writeln("type_id,")
            self.writeln(iftype + ",")
            self.writeln("&%s_info" % ifprefix)
            self.writeln(");")
            self.unindent()
            self.writeln()
        
        self.unindent()

        self.user_section("external_interfaces_register", 
                          "/* Register implementation of unmodeled interfaces... */"
                          )
        self.writeln()
        self.writeln("}")
        
        self.writeln()
        self.writeln("return type_id;")
        
        self.unindent()
        self.writeln()
        self.writeln("}")
        self.writeln()
        
    def _write_methods_implementation(self, visibility, comment=""):
        
        first = True
        
        for method in self._gobj.methods:
            
            if method.visibility != visibility:
                continue

            if first:
                first = False
                if comment:
                    self.writeln(comment)
                    self.writeln()
                    
            if method.visibility == Visibility.PUBLIC:
                self.annotations.write_method_annotation(self._gobj, method, self)
                            
            define_as_static = method.visibility == Visibility.PRIVATE
            self._write_method_lines(method,
                                     method.name, 
                                     implementation = True,
                                     define_as_static = define_as_static
                                     )
            if method.inheritance_mode == MethodInheritance.FINAL:
                self.user_section(method.name)
            else:
                self.writeln()
                self.indent()
                self.write("%(Class)sClass* cls = " % self._vars)
                self.writeln("%(NAMESPACE)s%(BASENAME)s_GET_CLASS(self);" % self._vars)
                self.writeln()
                args = ""
                for param in method.parameters:
                    if args:
                        args += ", "
                    args += param.name
                if args:
                    line = "cls->%s(self, %s);" % (method.name, args)
                else:
                    line = "cls->%s(self);" % method.name
                if method.result != types.NULL:
                    line = "return " + line
                self.writeln(line)
                self.unindent()
                self.writeln()
            self.writeln("}")
            self.writeln()
            
            if method.inheritance_mode == MethodInheritance.VIRTUAL:
                self._write_method_lines(method,
                                         method.name + "_im", 
                                         implementation = True,
                                         define_as_static = True
                                         )
                self.user_section(method.name)
                self.writeln("}")
                self.writeln()
                        
    def _write_method_decl(self, 
                           method, 
                           as_pointer = False, 
                           method_name = "",
                           define_as_static = False
                           ):
        
        self._write_method_lines(method, 
                                 method_name, 
                                 as_pointer, 
                                 implementation = False, 
                                 define_as_static = define_as_static                                 )

    def _write_method_impl(self, method, method_name="", define_as_static=True):

        self._write_method_lines(method, 
                                 method_name, 
                                 as_pointer = False, 
                                 implementation = True, 
                                 define_as_static = define_as_static
                                 )

    def _write_signal_decl(self, signal):
        
        self._declare_signal("%(Class)s" % self._vars, signal)
            
    def _write_add_signals(self):
        
        self._write_add_signal_section("%(Class)sClass" % self._vars)
        
    def _write_init_methods(self):

        if not self._gobj.abstract:
            self.writeln("/* ===== instance creation ===== */")
            self.writeln()
            self._write_method_decl(self._gobj.constructor)
            self.writeln()

    def _write_init_methods_prot(self):

        init_method = Method("init")
        init_method.parameters = self._gobj.constructor.parameters[:]

        self._write_method_decl(init_method)
        self.writeln()
        
    def _write_instantiation_impl(self):

        if not self._gobj.abstract:
            self._write_constructor_impl()
        
        init_method = Method("init")
        init_method.parameters = self._gobj.constructor.parameters[:]

        self._write_method_impl(init_method, define_as_static=False)
        self.user_section("constructor", "/* == init your members == */")
        self.writeln("}")
        self.writeln()
        self.writeln("void")
        self.writeln("%(prefix)s_dispose(GObject* obj) {" % self._vars)
        self.user_section("dispose", "/* unref ...*/")
        self.writeln("}")
        self.writeln()
        self.writeln("void")
        self.writeln("%(prefix)s_finalize(GObject* obj){" % self._vars)
        self.indent()
        self.writeln()
        if self._gobj.has_attributes(Visibility.PROTECTED):
            self.write(self.typename(self._gobj) + " self = ")
            self.writeln("%(NAMESPACE)s%(BASENAME)s(obj);" % self._vars)
            self.writeln()
        self.user_section("finalize", "/* free allocated memory... */")
        self.writeln()
        if self._gobj.has_attributes(Visibility.PROTECTED):
            self.writeln("g_free(self->prot);")
            self.writeln()
        self.unindent()
        self.writeln("}")
        self.writeln()
    
    def _write_constructor_impl(self):
        
        self.annotations.write_method_annotation(self._gobj, 
                                                 self._gobj.constructor, 
                                                 self
                                                 )
                                                         
        constructor = self._gobj.constructor
        self._write_method_impl(constructor, define_as_static=False)
        self.writeln()
        self.indent()
        
        self.write("%s obj = " % self.typename(self._gobj))
        self.write("g_object_new(")
        self.write("%(NAMESPACE)sTYPE_%(BASENAME)s" % self._vars)
        prop_inits = self._get_property_inits(constructor)
        if prop_inits:
            self.writeln(",")
            self.indent()
            for prop_name, prop_value in prop_inits:
                self.writeln('"%s", %s,' % (prop_name, prop_value))
            self.writeln("NULL")
            self.writeln(");")
            self.unindent()
        else:
            self.writeln(", NULL);")
        self.writeln()
        self.write("%(prefix)s_init(obj" % self._vars)
        if constructor.parameters:
            args=""
            for param in constructor.parameters:
                if args:
                    args += ", "
                args += param.name
            self.writeln(", " + args + ");")
        else:
            self.writeln(");")
        self.writeln()
        self.writeln("return obj;")
        self.unindent()
        self.writeln()
        self.writeln("}")
        self.writeln()    
        
    def _get_property_inits(self, constructor):
        
        res = []
        
        for param in constructor.parameters:
            if param.bind_to:
                res.append((param.bind_to, param.name)) 
                
        for prop_name in constructor.property_inits:
            val, is_code = constructor.property_inits[prop_name]
            if is_code:
                value = self._code_to_string(val)
            else:
                if val[0] == '"':
                    val = val[1:]
                if val[-1] == '"':
                    val = val[:-1]
                value = val.replace('\\"', '"')
            res.append((prop_name, value))
                
        return res
        
    def _write_method_decls(self, visibility, define_as_static=False):

        first = True
        for m in self._gobj.methods:
            if m.visibility != visibility:
                continue
            if first:
                first = False
                if visibility == Visibility.PUBLIC:
                    self.writeln("/* ===== public methods ===== */")
                elif visibility == Visibility.PROTECTED:
                    self.writeln("/* ===== protected methods ===== */")
                elif visibility == Visibility.PRIVATE:
                    self.writeln("/* ===== private methods ===== */")
            self.writeln()
            self._write_method_decl(m, define_as_static=define_as_static)
        if not first:
            self.writeln()

    def _write_method_impls(self, visibility):

        first = True
        for m in self._gobj.methods:
            if m.visibility != visibility:
                continue
            if first:
                first = False
                if visibility == Visibility.PUBLIC:
                    self.writeln("/* ===== public methods ===== */")
                elif visibility == Visibility.PROTECTED:
                    self.writeln("/* ===== protected methods ===== */")
                elif visibility == Visibility.PRIVATE:
                    self.writeln("/* ===== private methods ===== */")
            self.writeln()
            self._write_method_impl(m, m.name + "_im")
        if not first:
            self.writeln()
            
    def _write_interface_defs(self):
        
        self._write_interface_methods(implementation = False)
            
    def _write_interface_impls(self):
 
        self._write_interface_methods(implementation = True)
        
    def _write_interface_methods(self, implementation):
        
        first = True
        for intf in self._gobj.interfaces:
            for m in intf.methods:
                if first:
                    first = False
                    if implementation:
                        self.writeln("/* ===== interface methods (implementation) ===== */")
                    else:
                        self.writeln("/* ===== interface methods (definition) ===== */")
                self.writeln()
                
                method_name = self._func_name_creator.create_impl_func_name(m.name, intf.name)
                                    
                if implementation:
                    self._write_method_impl(m, 
                                            method_name
                                            )
                    section_name = intf.name + "_" + m.name
                    self.user_section(section_name)
                    self.writeln("}")
                else:
                    self.writeln("/* %s->%s */" % (intf.name, m.name))
                    self._write_method_decl(m, 
                                            as_pointer = False, 
                                            method_name = method_name,
                                            define_as_static = True
                                            )

        if not first:
            self.writeln()
            
    def _write_virtual_defs(self):
        
        first = True
        for m in self._gobj.methods:
            if m.inheritance_mode != MethodInheritance.VIRTUAL:
                continue
            if first:
                first = False
                self.writeln("/* ====== virtual methods (definition) ===== */")
            self.writeln()
            method_name = self._func_name_creator.create_impl_func_name(m.name)
            self._write_method_decl(m, 
                                    as_pointer = False, 
                                    method_name = method_name, 
                                    define_as_static = True
                                    )
        if not first:
            self.writeln()    
            
    def _write_overridden_defs(self):
        
        first = True
        
        for method_info in self._gobj.overridden_methods:
            
            if first:
                first = False
                self.writeln("/* ===== overridden methods (definition) ===== */")
                self.writeln()
            
            method_name = method_info.method.name + "_im"
            
            self._write_method_decl(method_info.method, 
                                    as_pointer = False, 
                                    method_name = method_name, 
                                    define_as_static = True
                                    )
            self.writeln()
            
    def _write_overridden_impls(self):
        
        first = True
        
        for method_info in self._gobj.overridden_methods:
            
            if first:
                first = False
                self.writeln("/* ===== overridden methods ===== */")
                self.writeln()
            
            method_name = method_info.method.name + "_im"
            
            self._write_method_impl(method_info.method, 
                                    method_name = method_name, 
                                    define_as_static = True
                                    )
            
            self.user_section(method_info.method.name)
            self.writeln("}")
            self.writeln()
                
    def _write_macros(self):

        self.writeln("/* ===== macros ===== */")
        self.writeln()

        self.writeln("#define %(NAMESPACE)sTYPE_%(BASENAME)s \\" % self._vars)
        self.indent()
        self.writeln("(%(prefix)s_get_type())" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)s%(BASENAME)s(obj) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_CHECK_INSTANCE_CAST((obj), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Class)s))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)s%(BASENAME)s_CLASS(cls) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_CHECK_CLASS_CAST((cls), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Class)sClass))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)sIS_%(BASENAME)s(obj) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_CHECK_INSTANCE_TYPE((obj), %(NAMESPACE)sTYPE_%(BASENAME)s))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)sIS_%(BASENAME)s_CLASS(cls) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_CHECK_CLASS_TYPE((cls), %(NAMESPACE)sTYPE_%(BASENAME)s))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)s%(BASENAME)s_GET_CLASS(obj) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_INSTANCE_GET_CLASS((obj), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Class)sClass))" % self._vars)
        self.unindent()

        self.writeln()

    def _basename(self):
        
        return self.to_underscore(self._gobj.name)
