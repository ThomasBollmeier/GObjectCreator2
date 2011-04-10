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

class Sections(object):
    """
    Abstract class to be inherited by all classes that implement
    user editable code sections
    """
    
    def __init__(self):
        
        if self.__class__ is Sections:
            raise NotImplementedError
        
        self._sections = {}
   
    def get_section_content(self, section_name):
        
        return self._sections[section_name]

    def _check_for_section_begin(self, line):
        """
        returns boolean flag indicating section begin, <name of section>, <first line or None>
        """
        raise NotImplementedError
        
    def _is_section_end(self, line):
        """
        returns True if section end is reached
        """
        raise NotImplementedError
           
    def _parse(self, file_path):
        
        self._sections = {}
        
        try:
            input_file = open(file_path, "r" )
        except IOError:
            return
        lines = input_file.readlines()
        input_file.close()
        
        in_user_section = False
        
        for line in lines:
            
            line = line[:-1] # remove line break
            
            if not in_user_section:
                section_begin, section_name, first_line = \
                    self._check_for_section_begin(line)
                if section_begin:
                    in_user_section = True
                    content = []
                    if first_line is not None:
                        content.append(first_line)
            else:
                if not self._is_section_end(line):
                    content.append(line)
                else:
                    self._sections[section_name] = content
                    in_user_section = False
                    section_name = ""
