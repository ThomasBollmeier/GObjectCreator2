# coding=UTF-8

import os
import subprocess
import gobjcreator2.metadef.types as types
from gobjcreator2.metadef.gobject import GObject
from gobjcreator2.metadef.genum import GEnum

class MarshallerGenerator(object):
    
    def __init__(self, clif):
        
        self._clif = clif
        self._prefix = self._clif.name.lower()
        package = self._clif.package
        while package:
            if package.name:
                self._prefix = package.name.lower() + "_" + self._prefix
            package = package.package
        
    def get_code(self, for_header = True):
        
        result = []
        
        lines = self._get_list_code()
        if not lines:
            return result
        
        input_name = "input%s" % os.getpid()
        input_file = open(input_name, "w")
        for line in lines:
            input_file.write(line + "\n")
        input_file.close()
            
        output_name = "output%s" % os.getpid()
        output_file = open(output_name, "w")
        
        if for_header:
            cmd = "cat %s | glib-genmarshal --prefix=%s --header" % (input_name, self._prefix)
        else:
            cmd = "cat %s | glib-genmarshal --prefix=%s --body" % (input_name, self._prefix)
            
        subprocess.call(cmd, shell=True, stdout=output_file)
        
        output_file.close()
        
        output_file = open(output_name, "r")
        
        result = [line.strip() for line in output_file.readlines()]
        
        output_file.close()
        
        os.remove(input_name)
        os.remove(output_name)
        
        return result
    
    def get_marshaller_name(self, signal):
        
        result = self._prefix
        
        result += "_" + self._get_marshaller_type(signal.result) + "__"
        
        if signal.parameters:
            args = ""
            for param in signal.parameters:
                if args:
                    args += "_"
                args += self._get_marshaller_type(param[1])
            result += args
        else:
            result += "VOID"
        
        return result
               
    def _get_list_code(self):
        
        result = []
        
        for signal in self._clif.signals:
            line = self._get_marshaller_type(signal.result) + ": "
            if signal.parameters:
                param_str = ""
                for param in signal.parameters:
                    if param_str:
                        param_str += ", "
                    param_str += self._get_marshaller_type(param[1])
            else:
                param_str = "VOID"
            line += param_str
            result.append(line)
            
        return result
    
    def _get_marshaller_type(self, type):
        
        if type is types.BOOL:
            res = "BOOLEAN"
        elif type is types.INT:
            res = "INT"
        elif type is types.UNSIGNED_INT:
            res = "UINT"
        elif type is types.LONG:
            res = "LONG"
        elif type is types.UNSIGNED_LONG:
            res = "ULONG"
        elif type is types.FLOAT:
            res = "FLOAT"
        elif type is types.DOUBLE:
            res = "DOUBLE"
        elif type is types.STRING:
            res = "STRING"
        elif type is types.POINTER:
            res = "POINTER"
        elif type is types.NULL:
            res = "VOID"
        elif isinstance(type, GObject):
            res = "OBJECT"
        elif isinstance(type, GEnum):
            res = "ENUM"
            
        return res        
        
                
  

    