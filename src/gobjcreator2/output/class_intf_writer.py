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


from gobjcreator2.output.writer import Writer, ListOut
from gobjcreator2.output.func_name_creator import FuncNameCreator
from gobjcreator2.output.annotations import Annotations
import gobjcreator2.output.util as util 
from gobjcreator2.output.marshaller_generator import MarshallerGenerator
from gobjcreator2.metadef.constants import *

class ClassIntfWriter(Writer):
    
    def __init__(self, object):
        
        Writer.__init__(self)
        
        self._obj = object
        self._func_name_creator = FuncNameCreator()
        self._base_prefix = util.camelcase_to_underscore(self._obj.prefix).lower()
        
        self.annotations = Annotations()
        
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

        if method.supportsFurtherParams:
            if args:
                args += ", "
            args += "..."

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
        
        if TypeModifier.CONST in signal.result_modifiers:
            modifiers = "const "
        else:
            modifiers = "" 

        self.writeln("%s%s /* %s */" % (modifiers,
                                        self.typename(signal.result),
                                        signal.name))
        self.write("(*%s)(" % signal.internal_name)
        
        args = "%s* sender" % sender_type_name
        if signal.parameters:
            args += ", "

        first_line_break = True
        for p in signal.parameters:
            if not TypeModifier.CONST in p[2]:
                tmp = ""
            else:
                tmp = "const "
            tmp += self.typename(p[1])
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

    def _write_signals_enum(self):
        
        if not self._obj.signals:
            return
        
        self.writeln("/* ===== signals ===== */")
        self.writeln()
        self.writeln("enum {")
        self.indent()
        for signal in self._obj.signals:
            self.writeln(signal.internal_name.upper() + ",")
        self.writeln("LAST_SIGNAL")
        self.unindent()
        self.writeln("};")
        self.writeln()
        self.writeln("static guint %(prefix)s_signals[LAST_SIGNAL] = {0};" % self._vars)
        self.writeln()

    def _write_add_signal_section(self, clif_class_name):
        
        if not self._obj.signals:
            return
        
        self.writeln("/* add signals */")
        self.writeln()
        
        marshaller_gen = MarshallerGenerator(self._obj)
        
        for signal in self._obj.signals:
            
            saved_out = self.output
            list_out = ListOut()
            self.output = list_out
            
            self.write("%(prefix)s_signals[" % self._vars)
            self.writeln("%s] = g_signal_new(\"%s\"," % (signal.internal_name.upper(), signal.name))
            self.indent()
            self.writeln(self.gtypename(self._obj) + ",")
            self.writeln("G_SIGNAL_RUN_LAST|G_SIGNAL_DETAILED,")
            self.write("G_STRUCT_OFFSET(%s, " % clif_class_name)
            self.writeln(signal.internal_name + "),")
            self.writeln("NULL, /* accumulator */")
            self.writeln("NULL,")
            self.writeln("%s," % marshaller_gen.get_marshaller_name(signal))
            self.writeln("%s," % self.gtypename(signal.result))
            if signal.parameters:
                self.writeln("%d," % len(signal.parameters))
                for param in signal.parameters:
                    self.write(self.gtypename(param[1]))
                    if not param is signal.parameters[-1]:
                        self.writeln(",")
                    else:
                        self.writeln()
            else:
                self.writeln("0")
            self.writeln(");")
            self.unindent()
                        
            self.output = saved_out
            
            self.user_section("signal_%s" % signal.internal_name,
                              default_code = list_out.get_lines(), 
                              indent_level = -1
                              )
            self.writeln()

    def write_marshaller_header(self):
        
        self._write_marshaller(header = True)

    def write_marshaller_source(self):
        
        self._write_marshaller(header = False)
        
    def _write_marshaller(self, header = True):
        
        marshaller_gen = MarshallerGenerator(self._obj)
        
        lines = marshaller_gen.get_code(for_header = header)
        for line in lines:
            self.writeln(line)
            
        self._writeln()
