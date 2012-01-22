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


from gobjcreator2.output.writer import Writer
import gobjcreator2.output.util as util

class GEnumWriter(Writer):
    
    def __init__(self, enum):
        
        Writer.__init__(self)
        
        self._enum = enum
        
        namespace = ""
        basename = util.camelcase_to_underscore(self._enum.name)
        
        package = self._enum.package
        while package:
            if package.name:
                namespace = package.name + "_" + namespace
            package = package.package
                
        self._vars = {
                      "NAMESPACE": namespace.upper(),
                      "BASENAME": basename.upper(),
                      "ENUM_ABS_NAME": namespace.upper() + basename.upper(),
                      "EnumAbsName": self.typename(self._enum),
                      "prefix": namespace.lower() + basename.lower()
                      }
                
    def write_header(self):
        
        self._write_comment()
        self.writeln()
        self.writeln("#ifndef %(ENUM_ABS_NAME)s_H" % self._vars)
        self.writeln("#define %(ENUM_ABS_NAME)s_H" % self._vars)
        self.writeln()
        self.writeln('#include "glib-object.h"')
        self.writeln()
        self.writeln("G_BEGIN_DECLS")
        self.writeln()
        self.writeln("typedef enum _%(EnumAbsName)s {" % self._vars)
        self.indent()
        self.writeln()
        last_idx = len(self._enum.code_values) - 1
        idx = 0
        for code, value in self._enum.code_values:
            self.write("%(ENUM_ABS_NAME)s_" % self._vars + code.upper())
            if value is not None:
                self.write(" = " + value)
            if idx != last_idx:
                self.writeln(",")
            else:
                self.writeln()
            idx += 1
        self.writeln() 
        self.unindent()
        self.writeln("} %(EnumAbsName)s;" % self._vars)
        self.writeln()
        self.writeln("GType")
        self.writeln("%(prefix)s_get_type();" % self._vars)
        self.writeln()
        self.write("#define %(NAMESPACE)sTYPE_%(BASENAME)s" % self._vars)
        self.writeln(" %(prefix)s_get_type()" % self._vars)
        self.writeln()
        self.writeln("G_END_DECLS")
        self.writeln()
        self.writeln("#endif")
        self.writeln()
   
    def write_source(self):

        self._write_comment()
        self.writeln()
        
        self.writeln('#include "%s"' % self._file_name_manager.get_header_name(self._enum))
        self.writeln()
        self.writeln("GType")
        self.writeln("%(prefix)s_get_type() {" % self._vars)
        self.indent()
        self.writeln()
        self.writeln("static GType type_id = 0;")
        self.writeln("GEnumValue* values;")
        self.writeln("guint idx;")
        self.writeln()
        self.writeln("if (type_id == 0) {")
        self.indent()
        self.writeln()
        num_codes = len(self._enum.code_values) + 1
        self.writeln("values = g_new(GEnumValue, %d);" % num_codes)
        self.writeln("idx = 0;")
        self.writeln()
        for code, value in self._enum.code_values:
            self.write("values[idx].value = ") 
            self.write("%(ENUM_ABS_NAME)s_" % self._vars)
            self.writeln("%s;" % code.upper())
            self.writeln('values[idx].value_name = "%s";' % code);
            self.writeln('values[idx].value_nick = "%s";' % code);
            self.writeln("idx++;")
            self.writeln()

        self.writeln("values[idx].value = 0;")
        self.writeln("values[idx].value_name = NULL;");
        self.writeln("values[idx].value_nick = NULL;");
        self.writeln()
        self.write("type_id = g_enum_register_static(")
        self.writeln('"%(EnumAbsName)s", values);' % self._vars)
        self.writeln()
        self.unindent()
        self.writeln("}")
        self.writeln()
        self.writeln("return type_id;")
        self.writeln()
        self.unindent()
        self.writeln("}")
        self.writeln()
