from gobjcreator2.output.writer import Writer
from gobjcreator2.output.func_name_creator import FuncNameCreator
from gobjcreator2.metadef.constants import Visibility, Scope, TypeModifier
from gobjcreator2.metadef.property import PropAccess
from gobjcreator2.metadef.method import Method, MethodInheritance

class GObjectWriter(Writer):

    def __init__(self, gobject):

        Writer.__init__(self)
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
            "prefix": namespace.lower() + self._gobj.prefix,
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
            self.writeln('#include "%s.h"' % \
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
        self._write_overriden_defs()
        self._write_method_decls(Visibility.PRIVATE)
        self._write_property_enum()
        self._write_signals_enum()
        
        self._write_class_init()
                
        self._write_interface_impls()
        
        self.user_section("source_bottom")
                    
    def _write_comment(self):

        self.writeln("/* This file has been generated automatically by GObjectCreator")
        self.writeln("* (see http://www.bollmeier.de/GObjectCreator for details).")
        self.writeln("* Please modify user sections only!")
        self.writeln("*/")

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
            self.write("* %s: \"%s\"" % (prop.name, prop.description))
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
     
    def _write_signals_enum(self):
        
        if not self._gobj.signals:
            return
        
        self.writeln("/* ===== signals ===== */")
        self.writeln()
        self.writeln("enum {")
        self.indent()
        for signal in self._gobj.signals:
            self.writeln(signal.internal_name.upper() + ",")
        self.writeln("LAST_SIGNAL")
        self.unindent()
        self.writeln("};")
        self.writeln()
        self.writeln("static guint %(prefix)s_signals[LAST_SIGNAL] = {0};" % self._vars)
        self.writeln()
        
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
                
        self.writeln()
        self.unindent()
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

    def _write_method_impl(self, method, method_name=""):

        self._write_method_lines(method, 
                                 method_name, 
                                 as_pointer = False, 
                                 implementation = True, 
                                 define_as_static = True
                                 )

    def _write_method_lines(self, 
                            method,
                            method_name, 
                            as_pointer = False,
                            implementation = False,
                            define_as_static = False
                            ):

        MAXLEN_ARG = 50
        
        if not method_name:
            name = method.name
        else:
            name = method_name
        
        tmp = self.typename(method.result)
        if TypeModifier.CONST in method.result_modifiers:
            tmp = "const " + tmp
        if define_as_static:
            tmp = "static " + tmp
        self.writeln(tmp)
        
        if not as_pointer:
            tmp = "%(prefix)s" % self._vars + "_" + name
        else:
            tmp = "(*%s)" % name
        self.write(tmp + "(")

        args = ""
        if method.scope == Scope.INSTANCE:
            if not method_name:
                lookup_method = method_name
                lookup_interface = ""
            else:
                lookup_method, lookup_interface = self._func_name_creator.get_info(method_name)
            method_info = self._gobj.lookup_method(lookup_method, lookup_interface)
            if method_info:
                selftype = self.typename(method_info.defined_in)
                if selftype == self.typename(self._gobj):
                    selfname = "self"
                else:
                    selfname = "obj"
            else:
                selftype = self.typename(self._gobj)
                selfname = "self"
            args += "%s %s" % (selftype, selfname) 
            if method.parameters:
                args += ", "

        first_line_break = True
        for p in method.parameters:
            tmp = self.typename(p.type)
            if TypeModifier.CONST in p.modifiers:
                tmp = "const " + tmp
            tmp += " " + p.name
            args += tmp
            is_last = p == method.parameters[-1]
            if not is_last:
                args += ", "
            if ( len(args) > MAXLEN_ARG ) and ( not is_last ):
                self.writeln(args)
                if first_line_break:
                    self.indent()
                    first_line_break = False
                args = ""

        if args:
            self.write(args)
            
        if not implementation:
            self.writeln(");")
        else:
            self.writeln(") {")
            
        if not first_line_break:
            self.unindent()

    def _write_signal_decl(self, signal):

        MAXLEN_ARG = 50

        self.writeln("%s /* %s */" % (self.typename(signal.result),
                                      signal.name))
        self.write("(*%s)(" % signal.internal_name)
        
        args = "%(Class)s* sender" % self._vars
        if signal.parameters:
            args += ", "

        first_line_break = True
        for p in signal.parameters:
            tmp = self.typename(p[1])
            tmp += " " + p[0]
            args += tmp
            is_last = p == signal.parameters[-1]
            if not is_last:
                args += ", "
            if ( len(args) > MAXLEN_ARG ) and ( not is_last ):
                self.writeln(args)
                if first_line_break:
                    self.indent()
                    first_line_break = False
                args = ""

        if args:
            self.write(args)
        self.writeln(");")

        if not first_line_break:
            self.unindent()

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

    def _write_method_decls(self, visibility):

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
            self._write_method_decl(m)
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
                    section_name = intf.name + "->" + m.name
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
            
    def _write_overriden_defs(self):
        
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

    def _clifname(self, clif):

        res = clif.name
        package = clif.package
        while package:
            if package.name:
                res = package.name.capitalize() + res
            package = package.package

        return res

    def _basename(self):

        res = ""
        lastChar = ""
        for ch in self._gobj.name:
            if lastChar:
                if lastChar == lastChar.lower() and ch == ch.upper():
                    res += "_"
            res += ch.upper()
            lastChar = ch
            
        return res

    def _filename_base(self, clif):

        return self._clifname(clif).lower()
