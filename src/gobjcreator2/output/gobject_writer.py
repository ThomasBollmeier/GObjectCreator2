from gobjcreator2.output.writer import Writer
from gobjcreator2.metadef.constants import Visibility, Scope

class GObjectWriter(Writer):

    def __init__(self, gobject):

        Writer.__init__(self)
        self._gobj = gobject

        self._vars = {
            "CLASS": self._clifname(self._gobj).upper(),
            "Class": self._clifname(self._gobj)
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

    def _clifname(self, clif):

        res = clif.name
        package = clif.package
        while package:
            if package.name:
                res = package.name.capitalize() + res
            package = package.package

        return res
