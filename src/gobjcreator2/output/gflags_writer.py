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

class GFlagsWriter(Writer):
    
    def __init__(self, flags):
        
        Writer.__init__(self)
        
        self._flags = flags
        
        namespace = ""
        basename = util.camelcase_to_underscore(self._flags.name)
        
        package = self._flags.package
        while package:
            if package.name:
                namespace = package.name + "_" + namespace
            package = package.package
                
        self._vars = {
                      "FLAGS_ABS_NAME": namespace.upper() + basename.upper(),
                      "FlagsAbsName": self.typename(self._flags),
                      }
                
    def write_header(self):
        
        self._write_comment()
        self.writeln()
        
        self.writeln("#ifndef %(FLAGS_ABS_NAME)s_H" % self._vars)
        self.writeln("#define %(FLAGS_ABS_NAME)s_H" % self._vars)
        self.writeln()
        self.writeln('#include "glib-object.h"')
        self.writeln()
        self.writeln("G_BEGIN_DECLS")
        self.writeln()
        self.writeln("typedef guint %(FlagsAbsName)s;" % self._vars)
        self.writeln()
        self.writeln("enum {")
        self.indent()
        self.writeln()
        shift = 0
        for code in self._flags.codes:
            self.write("%(FLAGS_ABS_NAME)s_" % self._vars)
            self.write("%s = 1 << %d" % (code, shift))
            shift += 1
            if code != self._flags.codes[-1]:
                self.write(",")
            self.writeln()
        self.writeln()
        self.unindent()
        self.writeln("};")
        self.writeln()
        self.writeln("G_END_DECLS")
        self.writeln()
        self.writeln("#endif")
        self.writeln()
