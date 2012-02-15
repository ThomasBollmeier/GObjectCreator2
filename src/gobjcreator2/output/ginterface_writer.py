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


from gobjcreator2.output.class_intf_writer import ClassIntfWriter
import gobjcreator2.output.util as util
from gobjcreator2.metadef.types import NULL

class GInterfaceWriter(ClassIntfWriter):

    def __init__(self, interface):

        ClassIntfWriter.__init__(self, interface)
        
        namespace = ""
        basename = util.camelcase_to_underscore(self._obj.name)
        
        package = self._obj.package
        while package:
            if package.name:
                namespace = package.name + "_" + namespace
            package = package.package
                
        self._vars = {
                      "Interface": self._clifname(self._obj),
                      "INTERFACE": self._clifname(self._obj).upper(),
                      "NAMESPACE": namespace.upper(),
                      "BASENAME": basename.upper(),
                      "prefix": namespace.lower() + self._base_prefix
                      }
        
    def write_header(self):
        
        self._write_comment()
        self.writeln()
        
        self.writeln("#ifndef %(INTERFACE)s_H" % self._vars)
        self.writeln("#define %(INTERFACE)s_H" % self._vars)
        self.writeln()
        if self._gobj.supports_further_params():
            self.writeln('#include <stdarg.h>')
        self.writeln('#include "glib-object.h"')
        self.writeln()
        self.writeln("G_BEGIN_DECLS")
        self.writeln()
        self.user_section("header_top", "/* add further includes.../")
        self.writeln()
        self._write_struct_defs()
        self.writeln("GType")
        self.writeln("%(prefix)s_get_type();" % self._vars)
        self.writeln()
        self._write_method_decls()
        self._write_macros()
        self.user_section("header_bottom")
        self.writeln()
        self.writeln("G_END_DECLS")
        self.writeln()
        self.writeln("#endif")
        self.writeln()
    
    def write_source(self):
        
        self._write_comment()
        self.writeln()
        
        self.writeln('#include "%s"' % self._file_name_manager.get_header_name(self._obj))
        self.writeln()
        
        lines = []
        if self._obj.signals:
            lines.append('#include "%s"' % \
                         self._file_name_manager.get_marshaller_header_name(self._obj))
        lines.append("/* add further includes... */")
        self.user_section("source_top", lines, indent_level = -1)
        self.writeln()
        
        self._write_signal_section()
        self._write_init_final_section()
        self._write_get_type_method()
        self._write_method_definitions()
        
        self.user_section("source_bottom")
        self.writeln()
        
    def _write_struct_defs(self):
        
        self.writeln("typedef struct _%(Interface)s %(Interface)s;" % self._vars)
        self.writeln()
        self.writeln("typedef struct _%(Interface)sIface {" % self._vars)
        self.indent()
        self.writeln()
        self.writeln("GTypeInterface base_interface;")
        self.writeln()
        
        first = True
        for method in self._obj.methods:
            if first:
                first = False
                self.writeln("/* == methods == */")
                self.writeln()
            self._write_method_lines(method, method.name, as_pointer=True)
        if not first:
            self.writeln()
            
        first = True
        for signal in self._obj.signals:
            if first:
                first = False
                self.writeln("/* == signals == */")
                self.writeln()
            self._write_signal_decl(signal)
        if not first:    
            self.writeln()
        
        self.unindent()
        self.writeln("} %(Interface)sIface;" % self._vars)
        self.writeln()    
        
    def _write_signal_decl(self, signal):
        
        self._declare_signal("%(Interface)s" % self._vars, signal)

    def _write_method_decls(self):
        
        if not self._obj.methods:
            return
        
        self.writeln("/* ===== methods ===== */")
        self.writeln()
        
        for method in self._obj.methods:
            self._write_method_lines(method, 
                                     method.name, 
                                     as_pointer = False, 
                                     implementation = False, 
                                     define_as_static = False
                                     ) 
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
        self.writeln("(G_TYPE_CHECK_INSTANCE_CAST((obj), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Interface)s))" % \
                     self._vars)
        self.unindent()
        self.writeln("#define %(NAMESPACE)s%(BASENAME)s_CLASS(cls) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_CHECK_CLASS_CAST((cls), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Interface)sIface))" % \
                     self._vars)
        self.unindent()
        self.writeln("#define %(NAMESPACE)sIS_%(BASENAME)s(obj) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_CHECK_INSTANCE_TYPE((obj), %(NAMESPACE)sTYPE_%(BASENAME)s))" % \
                     self._vars)
        self.unindent()
        self.writeln("#define %(NAMESPACE)s%(BASENAME)s_GET_CLASS(obj) \\" % self._vars)
        self.indent()
        self.writeln("(G_TYPE_INSTANCE_GET_INTERFACE((obj), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Interface)sIface))" % \
                     self._vars)
        self.unindent()
        self.writeln("#define %(NAMESPACE)s%(BASENAME)s_GET_INTERFACE(obj) \\" % \
                     self._vars)
        self.indent()
        self.write("(G_TYPE_INSTANCE_GET_INTERFACE((obj), ")
        self.writeln("%(NAMESPACE)sTYPE_%(BASENAME)s, %(Interface)sIface))" % \
                     self._vars)
        self.unindent()
        self.writeln()
        
    def _write_signal_section(self):
        
        if not self._obj.signals:
            return
        
        self._write_signals_enum()
        
    def _write_init_final_section(self):
        
        self.writeln("/* ===== initialization & finalization ===== */")
        self.writeln()
        
        self.writeln("static void")
        self.write("%(prefix)s_base_init(" % self._vars)
        self.writeln("%(Interface)sIface* iface) {" % self._vars)
        self.indent()
        self.writeln()
        self.writeln("static gboolean initialized = FALSE;")
        self.writeln()
        self.writeln("if (initialized)")
        self.indent()
        self.writeln("return;")
        self.unindent()
        self.writeln()
        self._write_add_signal_section("%(Interface)sIface" % self._vars)
        self.user_section("interface_init", "/* further initializations... */")
        self.writeln()
        self.writeln("initialized = TRUE;")
        self.writeln()
        self.unindent()
        self.writeln("}")
        self.writeln()
        
        self.writeln("static void")
        self.write("%(prefix)s_base_finalize(" % self._vars)
        self.writeln("%(Interface)sIface* iface) {" % self._vars)
        self.indent()
        self.writeln()
        self.writeln("static gboolean finalized = FALSE;")
        self.writeln()
        self.writeln("if (finalized)")
        self.indent()
        self.writeln("return;")
        self.unindent()
        self.writeln()
        self.user_section("interface_finalize", 
                          "/* do some final stuff... */"
                          )
        self.writeln()
        self.writeln("finalized = TRUE;")
        self.writeln()
        self.unindent()
        self.writeln("}")
        
        self.writeln()
    
    def _write_get_type_method(self):
        
        self.writeln("GType")
        self.writeln("%(prefix)s_get_type() {" % self._vars)
        self.indent()
        self.writeln()
        self.writeln("static GType type_id = 0;")
        self.writeln()
        self.writeln("if (type_id == 0) {")
        self.indent()
        self.writeln()
        self.writeln("const GTypeInfo %(prefix)s_info = {" % self._vars)
        self.indent()
        self.writeln("sizeof(%(Interface)sIface)," % self._vars)
        self.writeln("(GBaseInitFunc) %(prefix)s_base_init," % self._vars)
        self.writeln("(GBaseFinalizeFunc) %(prefix)s_base_finalize" % self._vars)
        self.writeln("};")
        self.unindent()
        self.writeln()
        self.writeln("type_id = g_type_register_static(")
        self.indent()
        self.writeln("G_TYPE_INTERFACE,")
        self.writeln('"%(Interface)s",' % self._vars)
        self.writeln("&%(prefix)s_info," % self._vars)
        self.writeln("0")
        self.writeln(");")
        self.writeln()
        self.unindent()
        self.writeln("/* all classes are allowed to implement this interface: */")
        self.writeln("g_type_interface_add_prerequisite(type_id, G_TYPE_OBJECT);")
        self.writeln()
        self.unindent()
        self.writeln("}")
        self.writeln()
        self.writeln("return type_id;")
        self.writeln()
        self.unindent()
        self.writeln("}")
        self.writeln()

    def _write_method_definitions(self):
        
        if not self._obj.methods:
            return
        
        self.writeln("/* ===== methods ===== */")
        self.writeln()
        
        for method in self._obj.methods:
            
            self.annotations.write_method_annotation(self._obj, method, self)
            
            self._write_method_lines(method, 
                                     method.name, 
                                     as_pointer = False, 
                                     implementation = True, 
                                     define_as_static = False
                                     )
            self.indent()
            self.writeln()
            self.write("%(Interface)sIface* iface = " % self._vars)
            self.writeln("%(NAMESPACE)s%(BASENAME)s_GET_INTERFACE(self);" % self._vars)
            self.writeln()
            call = "iface->%s(self" % method.name
            if method.parameters:
                args = ""
                for param in method.parameters:
                    if args:
                        args += ", "
                    args += param.name
                call += ", " + args
            call += ");"
            if method.result != NULL:
                call = "return " + call
            self.writeln(call)
            self.writeln()
            self.unindent()
            self.writeln("}")
            self.writeln()
