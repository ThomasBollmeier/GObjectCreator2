from gobjcreator2.output.writer import Writer
from gobjcreator2.output.func_name_creator import FuncNameCreator
import gobjcreator2.output.util as util 
from gobjcreator2.metadef.constants import *

class ClassIntfWriter(Writer):
    
    def __init__(self, object):
        
        Writer.__init__(self)
        self._obj = object
        self._func_name_creator = FuncNameCreator()
        self._base_prefix = util.camelcase_to_underscore(self._obj.prefix).lower()
        
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
            method_info = self._obj.lookup_method(lookup_method, lookup_interface)
            if method_info:
                selftype = self.typename(method_info.defined_in)
                if selftype == self.typename(self._obj):
                    selfname = "self"
                else:
                    selfname = "obj"
            else:
                selftype = self.typename(self._obj)
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

    def _declare_signal(self, sender_type_name, signal):

        MAXLEN_ARG = 50

        self.writeln("%s /* %s */" % (self.typename(signal.result),
                                      signal.name))
        self.write("(*%s)(" % signal.internal_name)
        
        args = "%s* sender" % sender_type_name
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
