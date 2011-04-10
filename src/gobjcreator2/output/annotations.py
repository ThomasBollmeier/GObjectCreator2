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

# coding=UTF-8

from gobjcreator2.output.sections import Sections
import gobjcreator2.output.util as util
from gobjcreator2.metadef.types import NULL
import re

class Annotations(Sections):
    """
    Defines user editable sections for GObjectIntrospection annotations
    """
    
    BEGIN_FIRST_LINE = re.compile(r"\s*/\*{2}\s*")
    BEGIN_SECOND_LINE = re.compile(r"\s*\*\s+(\w+):.*")
    END_LINE = re.compile(r"\s*\*/\s*")
    
    def __init__(self):
        
        Sections.__init__(self)
        self._first_matched = False
        
    @staticmethod
    def create_from_file(file_path):
        
        annotations = Annotations()
        annotations._parse(file_path)
        
        return annotations
    
    def load_from_file(self, file_path):
        
        self._first_matched = False
        self._parse(file_path)
            
    def write_method_annotation(self, clif, method, writer):
        
        prefix = util.namespace_prefix(clif)
        prefix += util.camelcase_to_underscore(clif.prefix).lower()
        
        section_name = prefix + "_" + method.name
        
        writer.writeln("/**")
        
        if section_name in self._sections:
            lines = self._sections[section_name]
            for line in lines:
                line = line.lstrip()
                writer.writeln(line)
        else:
            writer.writeln("* %s: " % section_name)
            writer.writeln("*")
            for param in method.parameters:
                writer.writeln("* @%s: ..." % param.name)
            if method.result is not NULL:
                writer.writeln("*")
                writer.writeln("* Return value: ...")
                        
        writer.writeln("*/")
        
    def _check_for_section_begin(self, line):
        """
        returns boolean flag indicating section begin, <name of section>
        """
        if not self._first_matched:
            if Annotations.BEGIN_FIRST_LINE.match(line):
                self._first_matched = True
            return False, "", None
        else:
            self._first_matched = False
            match = Annotations.BEGIN_SECOND_LINE.match(line)
            if match:
                return True, match.group(1), line
            else:
                return False, "", None
                
    def _is_section_end(self, line):
        """
        returns True if section end is reached
        """
        return bool(Annotations.END_LINE.match(line))

