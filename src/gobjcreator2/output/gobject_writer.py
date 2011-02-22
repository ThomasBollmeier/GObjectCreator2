from gobjcreator2.output.writer import Writer

class GObjectWriter(Writer):

    def __init__(self, gobject):

        Writer.__init__(self)
        self._gobj = gobject

    def write_header(self):

        self._write_comment()
        self.writeln()

        self.writeln("#ifndef %s_H" % self._classname(self._gobj).upper())
        self.writeln("#define %s_H" % self._classname(self._gobj).upper())
        self.writeln()
        self.writeln('#include "glib-object.h"')
        self.writeln()
        self.writeln("G_BEGIN_DECLS")
        self.writeln()

        if self._gobj.super_class:
            self.writeln('#include "%s.h"' % \
                         self._classname(self._gobj.super_class).lower())
            self.writeln()

        self.user_section("header_top")

        self.writeln()
        self.writeln("G_END_DECLS")
        self.writeln()
        self.writeln("#endif")

    def _write_comment(self):

        self.writeln("/* This file has been generated automatically by GObjectCreator")
        self.writeln("* (see http://www.bollmeier.de/GObjectCreator for details).")
        self.writeln("* Please modify user sections only!")
        self.writeln("*/")

    def _classname(self, cls):

        res = cls.name
        package = cls.package
        while package:
            if package.name:
                res = package.name.capitalize() + res
            package = package.package

        return res
