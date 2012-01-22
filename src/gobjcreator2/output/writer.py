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


import gobjcreator2.metadef.types as types
from gobjcreator2.metadef.gobject import GObject
from gobjcreator2.metadef.ginterface import GInterface
from gobjcreator2.metadef.package import PackageElement, Package
import gobjcreator2.output.util as util
from gobjcreator2.output.user_content import UserContent
from gobjcreator2.output.file_name_manager import get_file_name_manager

class Output(object):
    
    def __init__(self):
        pass

    def wrt(self, text):

        raise NotImplementedError

class StdOut(Output):
    
    def __init__(self):
        
        Output.__init__(self)
        
    def wrt(self, text):

        print text
        
class ListOut(Output):

    def __init__(self):
        
        Output.__init__(self)
        
        self._lines = []
    
    def wrt(self, text):
        
        self._lines.append(text)
        
    def get_lines(self):
        
        return self._lines
    
class NullOut(Output):
    
    def __init__(self):
        
        Output.__init__(self)
        
    def wrt(self, text):
        
        pass
    
class FileOut(Output):
    
    def __init__(self, file_path):
        
        Output.__init__(self)
        
        self._file_path = file_path
        
    def open(self):
        
        self._file = open(self._file_path, "w")
        
    def close(self):
        
        self._file.close()
        
    def wrt(self, text):
        
        self._file.write(text + "\n")
        
class Writer(object):

    def __init__(self):

        self._indent = 0
        self._tab_size = 4
        self._begin_of_line = True
        self._line = ""
        
        self._output = StdOut()
        self._user_content = None
        self._header_comment = []
        self._file_name_manager = get_file_name_manager()

    def set_output(self, output):

        self._output = output
        
    def get_output(self):
        
        return self._output
    
    output = property(get_output, set_output)
    
    def set_header_comment(self, lines):
        
        self._header_comment = lines
            
    def set_user_content(self, file_path):
        
        self._user_content = UserContent.create_from_file(file_path)
        
    def set_file_name_manager(self, file_name_manager):
        
        self._file_name_manager = file_name_manager
        
    def set_tab_size(self, size):

        self._tab_size = size

    def write(self, text):

        if self._begin_of_line:
            tmp = " " * self._indent + text
            self._begin_of_line = False
        else:
            tmp = text
        self._line += tmp

    def writeln(self, text=""):

        if self._begin_of_line:
            tmp = " " * self._indent + text
            self._begin_of_line = False
        else:
            tmp = text
        self._line += tmp
        self._output.wrt(self._line)
        self._begin_of_line = True
        self._line = ""

    def user_section(self, name, default_code=None, indent_level=1):

        self.writeln("/* UserCode %s { */" % name)
        
        # Insert user code if it has already been modified:
        try:
            
            user_lines = self._user_content.get_section_content(name)
            
            saved_indent = self._indent
            self._indent = 0
            
            for line in user_lines:
                self.writeln(line)
        
            self._indent = saved_indent
        
        except KeyError: # -> user section has not been in use before:
        
            if default_code is not None:
             
                self.writeln()
                
                if indent_level > 0:
                    for dum in range(indent_level):
                        self.indent()
                elif indent_level < 0:
                    for dum in range(abs(indent_level)):
                        self.unindent()
                    
                if isinstance(default_code, str):
                    lines = default_code.split("\n")
                elif isinstance(default_code, list):
                    lines = default_code
                else:
                    lines = []
                
                for line in lines:
                    self.writeln(line)
            
                if indent_level > 0:
                    for dum in range(indent_level):
                        self.unindent()
                elif indent_level < 0:
                    for dum in range(abs(indent_level)):
                        self.indent()
    
                self.writeln()
            
            else:
            
                self.writeln()
        
        self.writeln("/* } UserCode */")

    def indent(self):

        self._indent += self._tab_size

    def unindent(self):

        self._indent -= self._tab_size

    def typename(self, type):

        if isinstance(type, types.RefType):
            res = self.typename(type.ref_type) + "*"
        elif isinstance(type, types.ListType):
            res = self.typename(type.line_type) + "*"
        elif type is types.BOOL:
            res = "gboolean"
        elif type is types.BYTE:
            res = "guchar"
        elif type is types.INT:
            res = "gint"
        elif type is types.UNSIGNED_INT:
            res = "guint"
        elif type is types.LONG:
            res = "glong"
        elif type is types.UNSIGNED_LONG:
            res = "gulong"
        elif type is types.FLOAT:
            res = "gfloat"
        elif type is types.DOUBLE:
            res = "gdouble"
        elif type is types.STRING:
            res = "gchar*"
        elif type is types.POINTER:
            res = "gpointer"
        elif type is types.NULL:
            res = "void"
        elif isinstance(type, PackageElement):
            res = type.name
            p = type.package
            while p:
                if p.name:
                    res = p.name.capitalize() + res
                p = p.package
            if isinstance(type, GObject) or isinstance(type, GInterface):
                res += "*"

        return res

    def gtypename(self, typename_or_type, current_package=None):
        
        if isinstance(typename_or_type, types.Type):
            type = typename_or_type
        else:
            if not current_package:
                current_package = Package.get_top()
            type = current_package[typename_or_type]
            
        return util.gtypename(type)

    def to_underscore(self, name):
        
        return util.camelcase_to_underscore(name)

    def _write_comment(self):
        
        if not self._header_comment:
            self.writeln("/* This file has been generated automatically by GObjectCreator")
            self.writeln("* (see http://www.bolles-werk.org/software-projects/gobjectcreator.html for details).")
            self.writeln("* Please modify user sections only!")
            self.writeln("*/")
        else:
            for line in self._header_comment:
                self.writeln(line)
        
    def file_basename(self, element):
        
        res = util.camelcase_to_underscore(element.name).lower()
        
        package = element.package
        while package:
            if package.name:
                res = package.name.lower() + "_" + res
            package = package.package
        
        return res

    def _filename_base(self, clif):
        
        return self.file_basename(clif)

    def _clifname(self, clif):
        
        return util.clifname(clif)
