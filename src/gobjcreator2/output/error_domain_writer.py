from gobjcreator2.output.writer import Writer
import gobjcreator2.output.util as util

class ErrorDomainWriter(Writer):
    
    def __init__(self, error_domain):
        
        Writer.__init__(self)
        
        self._error = error_domain
        
        namespace = ""
        basename = util.camelcase_to_underscore(self._error.name)
        error_domain_name = self._error.name
        
        package = self._error.package
        while package:
            if package.name:
                namespace = package.name + "_" + namespace
                error_domain_name = package.name.capitalize() + error_domain_name
            package = package.package
                
        self._vars = {
                      "ERROR_DOMAIN_NAME": namespace.upper() + basename.upper(),
                      "error_domain_name": namespace.lower() + basename.lower(),
                      "ErrorDomainName": error_domain_name,
                      }
        
    def write_header(self):
        
        self._write_comment()
        self.writeln()
        
        self.writeln("#ifndef %(ERROR_DOMAIN_NAME)s_H" % self._vars)
        self.writeln("#define %(ERROR_DOMAIN_NAME)s_H" % self._vars)
        self.writeln()
        self.writeln('#include "glib-object.h"')
        self.writeln()
        self.writeln("G_BEGIN_DECLS")
        self.writeln()
        self.write("#define %(ERROR_DOMAIN_NAME)s " % self._vars) 
        self.write("g_quark_from_static_string(")
        self.writeln('"%(error_domain_name)s_quark")' % self._vars)
        self.writeln()
        self.writeln("enum %(ErrorDomainName)s {" % self._vars)
        self.indent()
        self.writeln()
        first = True
        for error_code in self._error.error_codes:
            self.write("%(ERROR_DOMAIN_NAME)s_" % self._vars)
            self.write(error_code.upper())
            if first:
                first = False
                self.write(" = 1")
            if error_code != self._error.error_codes[-1]:
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
        