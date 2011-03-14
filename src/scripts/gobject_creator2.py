import sys
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
import os

class CodeGenerator(object):
    
    def __init__(self):
        
        self._outdir = os.curdir

    def create_code(self, elem):
        
        if isinstance(elem, Package):
            
            for el in elem.elements.values():
                self.create_code(el)
        
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
        
        self._write_header(writer, elem)
        self._write_protected_header(writer, elem)
        
        self._write_source(writer, elem)
        
        if elem.signals:
            self._write_marshaller_code(writer, elem, for_header = True)
            self._write_marshaller_code(writer, elem, for_header = False)
                            
    def _create_code_interface(self, elem):
        
        writer = GInterfaceWriter(elem)
        
        self._write_header(writer, elem)
        
        self._write_source(writer, elem)

        if elem.signals:
            self._write_marshaller_code(writer, elem, for_header = True)
            self._write_marshaller_code(writer, elem, for_header = False)
    
    def _create_code_enumeration(self, elem):
        
        writer = GEnumWriter(elem)
        
        self._write_header(writer, elem)
        
        self._write_source(writer, elem)

    def _create_code_flags(self, elem):
        
        writer = GFlagsWriter(elem)
        
        self._write_header(writer, elem)
        
    def _create_code_error_domain(self, elem):
        
        writer = ErrorDomainWriter(elem)
        
        self._write_header(writer, elem)
        
    def _write_header(self, writer, elem):
        
        basename = writer.file_basename(elem)
        file_out = FileOut(self._outdir + os.sep + basename + ".h")
        
        saved_out = writer.get_output()
        writer.set_output(file_out)
        
        file_out.open()
        writer.write_header()
        file_out.close()
        
        writer.set_output(saved_out)

    def _write_protected_header(self, writer, elem):
        
        basename = writer.file_basename(elem)
        file_out = FileOut(self._outdir + os.sep + basename + "_prot.h")
        
        saved_out = writer.get_output()
        writer.set_output(file_out)
        
        file_out.open()
        writer.write_header_protected()
        file_out.close()
        
        writer.set_output(saved_out)

    def _write_source(self, writer, elem):
        
        basename = writer.file_basename(elem)
        file_out = FileOut(self._outdir + os.sep + basename + ".c")
        
        saved_out = writer.get_output()
        writer.set_output(file_out)
        
        file_out.open()
        writer.write_source()
        file_out.close()
        
        writer.set_output(saved_out)
      
    def _write_marshaller_code(self, writer, elem, for_header):
        
        basename = writer.file_basename(elem)
        if for_header:
            file_out = FileOut(self._outdir + os.sep + basename + "_marshaller.h")
        else:
            file_out = FileOut(self._outdir + os.sep + basename + "_marshaller.c")
            
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
                
##### main #####

args = sys.argv[1:]
if len(args) != 1:
    exit(1)
    
goc_file = args[0]

recognizer = GOCRecognizer()
root_package = recognizer.process_file(goc_file)

code_gen = CodeGenerator()
code_gen.create_code(root_package)
    
exit(0)
