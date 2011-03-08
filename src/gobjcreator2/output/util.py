# coding=UTF-8

import gobjcreator2.metadef.types as types
from gobjcreator2.metadef.package import PackageElement

def gtypename(type):
    
        if type is types.BOOL:
            res = "G_TYPE_BOOLEAN"
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
            if lastChar == lastChar.lower() and ch == ch.upper():
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