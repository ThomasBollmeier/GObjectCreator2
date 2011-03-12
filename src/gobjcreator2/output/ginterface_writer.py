from gobjcreator2.output.class_intf_writer import ClassIntfWriter
import gobjcreator2.output.util as util

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
    
    def write_source(self):
        
        pass

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
        