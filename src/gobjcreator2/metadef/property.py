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


class Property(object):

    def __init__(self,
        name,
        type,
        access,
        description,
        gtype,
        min,
        max,
        default,
        auto_create
        ):

        self.name = name
        self.type = type
        self.access = access
        self.description = description
        self.gtype = gtype
        self.min = min
        self.max = max
        self.default = default
        self.auto_create = auto_create

class PropType:

    BOOLEAN = 1
    INTEGER = 2
    FLOAT = 3
    DOUBLE = 4
    STRING = 5
    POINTER = 6
    OBJECT = 7
    ENUMERATION = 8

class PropAccess:

    READ_ONLY = 1
    INITIAL_WRITE = 2
    READ_WRITE = 3

class PropGTypeValue(object):

    def __init__(self, name, is_typename):

        self.name = name
        self.is_typename = is_typename
        
class PropValue(object):
    
    def __init__(self, name, is_codename):
        
        self.name = name
        self.is_codename = is_codename
