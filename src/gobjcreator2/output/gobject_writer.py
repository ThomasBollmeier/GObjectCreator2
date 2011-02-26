from gobjcreator2.output.writer import Writer
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
                         self._clifname(self._gobj.super_class).lower())

        for intf in self._gobj.interfaces:
            self.writeln('#include "%s.h"' % self._clifname(intf).lower())
        self.writeln()

        self.user_section("header_top", "/* add includes here... */")
        self.writeln()

        if self._gobj.has_attributes(Visibility.PRIVATE):
            self.writeln("typedef struct _%(Class)sPriv %(Class)sPriv;" % self._vars)
        if self._gobj.has_attributes(Visibility.PROTECTED):
            self.writeln("typedef struct _%(Class)sProt %(Class)sProt;" % self._vars)
        self.writeln()

        self._write_struct()
        
        self._write_class_struct()

        self.writeln("GType %(prefix)s_get_type();" % self._vars)
        self.writeln()

        self._write_init_methods()

        self._write_public_method_decls()
        
        self._write_properties()

        self._write_macros()

        self.writeln("G_END_DECLS")
        self.writeln()
        self.writeln("#endif")

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
                self.writeln("/* public */")
            elif attr.visibility == Visibility.PROTECTED:
                self.writeln("/* protected */")
            elif attr.visibility == Visibility.PRIVATE:
                self.writeln("/* private */")

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

    def _write_method_decl(self, method, as_pointer=False):

        MAXLEN_ARG = 50

        tmp = self.typename(method.result)
        if TypeModifier.CONST in method.result_modifiers:
            tmp = "const " + tmp
        self.writeln(tmp)
        if not as_pointer:
            tmp = "%(prefix)s" % self._vars + "_" + method.name
        else:
            tmp = "(*%s)" % method.name
        self.write(tmp + "(")

        args = ""
        if method.scope == Scope.INSTANCE:
            args += "%(Class)s* self" % self._vars
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
        self.writeln(");")

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
            self.writeln("/* ===== instance creation & destruction ===== */")
            self.writeln()
            self._write_method_decl(self._gobj.constructor)
            self.writeln()

    def _write_public_method_decls(self):

        first = True
        for m in self._gobj.methods:
            if m.visibility != Visibility.PUBLIC:
                continue
            if first:
                first = False
                self.writeln("/* ===== public methods ===== */")
            self.writeln()
            self._write_method_decl(m)
        if not first:
            self.writeln()

    def _write_macros(self):

        self.writeln("/* ===== macros ===== */")
        self.writeln()

        self.writeln("#define %(NAMESPACE)sTYPE_%(BASENAME)s \\" % \
            self._vars)
        self.indent()
    	self.writeln("(%(prefix)s_get_type())" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)s%(BASENAME)s(obj) \\" % \
            self._vars)
        self.indent()
    	self.writeln("(G_TYPE_CHECK_INSTANCE_CAST((obj), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Class)s))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)s%(BASENAME)s_CLASS(cls) \\" % \
            self._vars)
        self.indent()
    	self.writeln("(G_TYPE_CHECK_CLASS_CAST((cls), %(NAMESPACE)sTYPE_%(BASENAME)s, %(Class)sClass))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)sIS_%(BASENAME)s(obj) \\" % \
            self._vars)
        self.indent()
    	self.writeln("(G_TYPE_CHECK_INSTANCE_TYPE((obj), %(NAMESPACE)sTYPE_%(BASENAME)s))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)sIS_%(BASENAME)s_CLASS(cls) \\" % \
            self._vars)
        self.indent()
    	self.writeln("(G_TYPE_CHECK_CLASS_TYPE((cls), %(NAMESPACE)sTYPE_%(BASENAME)s))" % self._vars)
        self.unindent()

        self.writeln("#define %(NAMESPACE)s%(BASENAME)s_GET_CLASS(obj) \\" % \
            self._vars)
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

