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

import re

class UserContent(object):
    
    STYLES = COMMENT_C, COMMENT_CPP = list(range(2))
    
    def __init__(self):
        
        self._sections = {}
        self.set_comment_style(UserContent.COMMENT_C)
   
    def get_section_content(self, section_name):
        
        return self._sections[section_name]
        
    def set_comment_style(self, style):
        
        if style == UserContent.COMMENT_C:
            self._re_block_begin = \
                re.compile(r"\s*/\*\s*UserCode\s+(\w*)\s*{\s*\*/")
            self._re_block_end = \
                re.compile(r"\s*/\*\s*}\s*UserCode\s*\*/")
        elif style == UserContent.COMMENT_CPP:
            self._re_block_begin = \
                re.compile(r"\s*//\s*UserCode\s+(\w*)\s*{\s*")
            self._re_block_end = \
                re.compile(r"\s*//\s*}\s*UserCode\s*")
        else:
            return
        
        self._style = style
        
    @staticmethod
    def create_from_file(file_path):
        
        res = UserContent()
        res._parse(file_path)
        
        return res

    def _check_for_section_begin(self, line):
        
        match = self._re_block_begin.match(line)
        if match:
            return True, match.group(1)
        else:
            return False, ""

    def _is_section_end(self, line):
        
        match = self._re_block_end.match(line)
        if match:
            return True
        else:
            return False
        
    def _parse(self, file_path):
        
        self._sections = {}
        
        try:
            input_file = open(file_path, "r" )
        except IOError:
            return
        lines = input_file.readlines()
        input_file.close()
        
        user_code = False
        
        for line in lines:
            
            line = line[:-1] # Zeilenumbruch entfernen
            
            if not user_code:
                section_begin, section_name = \
                    self._check_for_section_begin(line)
                if section_begin:
                    user_code = True
                    user_lines = []
            else:
                if not self._is_section_end(line):
                    user_lines.append(line)
                else:
                    self._sections[section_name] = user_lines
                    user_code = False
                    section_name = ""
