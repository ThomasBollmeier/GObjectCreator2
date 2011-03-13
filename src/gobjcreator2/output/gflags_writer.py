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
