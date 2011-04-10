#!/usr/bin/python
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

import sys
from optparse import OptionParser
import os

from gobjcreator2.input.goc_recognizer import GOCRecognizer
from gobjcreator2.metadef.package import Package
from gobjcreator2.metadef.gobject import GObject
from gobjcreator2.metadef.ginterface import GInterface
from gobjcreator2.metadef.genum import GEnum
from gobjcreator2.metadef.gflags import GFlags
from gobjcreator2.metadef.error_domain import ErrorDomain
from gobjcreator2.output.writer import FileOut
from gobjcreator2.output.gobject_writer import GObjectWriter
from gobjcreator2.output.ginterface_writer import GInterfaceWriter
from gobjcreator2.output.genum_writer import GEnumWriter
from gobjcreator2.output.gflags_writer import GFlagsWriter
from gobjcreator2.output.error_domain_writer import ErrorDomainWriter
from gobjcreator2.output.marshaller_generator import MarshallerGenerator
from gobjcreator2 import VERSION

def _create_option_parser():
    
    res = OptionParser(usage = "usage: %prog [options] <goc_file>", 
                       version = "%%prog, Version: %s, Author: Thomas Bollmeier" % \
                       VERSION
                       )
    
    res.add_option("-d", "--dir",
                   dest = "outdir",
                   default = os.curdir,
                   metavar = "DIR",
                   help = "generate files in directory DIR"
                   )

    res.add_option("-r", "--root",
                   dest = "root",
                   default = "",
                   metavar = "ROOT_NAME",
                   help = "generate objects of subtree ROOT_NAME only"
                   )
        
    res.add_option("-I", "--include",
                   action = "append",
                   dest = "include_paths",
                   default = [],
                   metavar = "DIR",
                   help = "add DIR to search path for definition files"
                   )
    
    res.add_option("-v",
                   action = "store_true",
                   dest = "verbose",
                   default = False,
                   help = "write generation info to standard output"
                   )
    
    res.add_option("", "--header-comment",
                   dest = "header_comment_file",
                   default = "",
                   metavar = "FILE",
                   help = "add header comment from FILE to generated code"
                   )
            
    return res

class CodeGenerator(object):
    
    def __init__(self):
        
        self._outdir = os.curdir
        self._comment_lines = []
        self.verbose = False
        
    def set_output_dir(self, outdir):
        
        self._outdir = outdir
        
    def set_header_comment_from_file(self, file_path):
        
        f = open(file_path, "r")
        
        self._comment_lines = []
        
        for line in f.readlines():
            self._comment_lines.append(line.strip("\n"))
        
        f.close()
        
    def _init_writer(self, writer):
        
        if self._comment_lines:
            writer.set_header_comment(self._comment_lines)

    def create_code(self, elem):
        
        if not os.path.exists(self._outdir):
            os.mkdir(self._outdir)
                    
        self._create_code(elem)
        
    def _create_code(self, elem):
        
        if isinstance(elem, Package):
            
            for el in elem.elements.values():
                self._create_code(el)
        
        else:
            
            # skip elements from included goc files:
            if elem.is_external:
                return
            
            if isinstance(elem, GObject):
                self._create_code_object(elem)
            elif isinstance(elem, GInterface):
                self._create_code_interface(elem)
            elif isinstance(elem, GEnum):
                self._create_code_enumeration(elem)
            elif isinstance(elem, GFlags):
                self._create_code_flags(elem)
            elif isinstance(elem, ErrorDomain):
                self._create_code_error_domain(elem)    
                
    def _create_code_object(self, elem):
        
        writer = GObjectWriter(elem)
        self._init_writer(writer)
        
        self._write_header(writer, elem)
        self._write_protected_header(writer, elem)
        
        self._write_source(writer, elem)
        
        if elem.signals:
            self._write_marshaller_code(writer, elem, for_header = True)
            self._write_marshaller_code(writer, elem, for_header = False)
                            
    def _create_code_interface(self, elem):
        
        writer = GInterfaceWriter(elem)
        self._init_writer(writer)
        
        self._write_header(writer, elem)
        
        self._write_source(writer, elem)

        if elem.signals:
            self._write_marshaller_code(writer, elem, for_header = True)
            self._write_marshaller_code(writer, elem, for_header = False)
    
    def _create_code_enumeration(self, elem):
        
        writer = GEnumWriter(elem)
        self._init_writer(writer)
        
        self._write_header(writer, elem)
        
        self._write_source(writer, elem)

    def _create_code_flags(self, elem):
        
        writer = GFlagsWriter(elem)
        self._init_writer(writer)
        
        self._write_header(writer, elem)
        
    def _create_code_error_domain(self, elem):
        
        writer = ErrorDomainWriter(elem)
        self._init_writer(writer)
        
        self._write_header(writer, elem)
        
    def _write_header(self, writer, elem):
        
        basename = writer.file_basename(elem)
        file_path = self._outdir + os.sep + basename + ".h"
        
        if self.verbose:
            print "generating file %s..." % file_path,
        
        writer.set_user_content(file_path)
        
        file_out = FileOut(file_path)
        
        saved_out = writer.get_output()
        writer.set_output(file_out)
                
        file_out.open()
        writer.write_header()
        file_out.close()
        
        writer.set_output(saved_out)
        
        if self.verbose:
            print "done"

    def _write_protected_header(self, writer, elem):
        
        basename = writer.file_basename(elem)
        file_path = self._outdir + os.sep + basename + "_prot.h"

        if self.verbose:
            print "generating file %s..." % file_path,
        
        writer.set_user_content(file_path)
        
        file_out = FileOut(file_path)
        
        saved_out = writer.get_output()
        writer.set_output(file_out)
        
        file_out.open()
        writer.write_header_protected()
        file_out.close()
        
        writer.set_output(saved_out)

        if self.verbose:
            print "done"

    def _write_source(self, writer, elem):
        
        basename = writer.file_basename(elem)
        file_path = self._outdir + os.sep + basename + ".c"

        if self.verbose:
            print "generating file %s..." % file_path,
        
        writer.set_user_content(file_path)
        
        if isinstance(writer, GObjectWriter) or isinstance(writer, GInterfaceWriter):
            writer.annotations.load_from_file(file_path)
        
        file_out = FileOut(file_path)
        
        saved_out = writer.get_output()
        writer.set_output(file_out)
        
        file_out.open()
        writer.write_source()
        file_out.close()
        
        writer.set_output(saved_out)

        if self.verbose:
            print "done"
      
    def _write_marshaller_code(self, writer, elem, for_header):
        
        basename = writer.file_basename(elem)
        if for_header:
            file_path = self._outdir + os.sep + basename + "_marshaller.h"
            file_out = FileOut(file_path)
        else:
            file_path = self._outdir + os.sep + basename + "_marshaller.c"
            file_out = FileOut(file_path)

        if self.verbose:
            print "generating file %s..." % file_path,
            
        saved_out = writer.get_output()
        writer.set_output(file_out)
        
        file_out.open()
        
        marshaller_gen = MarshallerGenerator(elem)
        lines = marshaller_gen.get_code(for_header)
        
        for line in lines:
            writer.writeln(line)
        writer.writeln()
        file_out.close()
        
        writer.set_output(saved_out)
        
        if self.verbose:
            print "done"
                
##### main #####

parser = _create_option_parser()

options, args = parser.parse_args()

if not len(args) == 1:
    exit(1)
    
goc_file = args[0]

recognizer = GOCRecognizer()
for path in options.include_paths:
    recognizer.add_include_path(path)

top_package = recognizer.process_file(goc_file)
if not options.root:
    root_elem = top_package
else:
    root_elem = top_package[options.root]

code_gen = CodeGenerator()
code_gen.set_output_dir(options.outdir)
code_gen.verbose = options.verbose
if options.header_comment_file:
    code_gen.set_header_comment_from_file(options.header_comment_file)
    
code_gen.create_code(root_elem)
    
exit(0)
