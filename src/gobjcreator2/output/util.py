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

import gobjcreator2.metadef.types as types
from gobjcreator2.metadef.package import PackageElement

def gtypename(type):
    
        if type is types.BOOL:
            res = "G_TYPE_BOOLEAN"
        elif type is types.BYTE:
            res = "G_TYPE_UCHAR"
        elif type is types.INT:
            res = "G_TYPE_INT"
        elif type is types.UNSIGNED_INT:
            res = "G_TYPE_UINT"
        elif type is types.LONG:
            res = "G_TYPE_LONG"
        elif type is types.UNSIGNED_LONG:
            res = "G_TYPE_ULONG"
        elif type is types.FLOAT:
            res = "G_TYPE_FLOAT"
        elif type is types.DOUBLE:
            res = "G_TYPE_DOUBLE"
        elif type is types.STRING:
            res = "G_TYPE_STRING"
        elif type is types.POINTER:
            res = "G_TYPE_POINTER"
        elif type is types.NULL:
            res = "G_TYPE_NONE"
        elif isinstance(type, PackageElement):
            res = "TYPE_%s" % camelcase_to_underscore(type.name)
            p = type.package
            while p:
                if p.name:
                    res = p.name.upper() + "_" + res
                p = p.package

        return res
    
def camelcase_to_underscore(name):

    res = ""
    lastChar = ""
    for ch in name:
        if lastChar:
            if lastChar == lastChar.lower() and ch == ch.upper() and ch != "_":
                res += "_"
        res += ch.upper()
        lastChar = ch
        
    return res

def namespace_prefix(element):
    
    res = ""
    package = element.package
    while package:
        if package.name:
            if not res:
                res = package.name
            else:
                res = package.name + "_" + res
        package = package.package
        
    if res:
        res += "_"
        
    return res

def clifname(class_or_intf):
    """
    Returns name of a class or interface
    """
    
    res = class_or_intf.name
    package = class_or_intf.package
    while package:
        if package.name:
            res = package.name.capitalize() + res
        package = package.package

    return res
