from gobjcreator2.input.goc_recognizer import GOCRecognizer
from gobjcreator2.output.gobject_writer import GObjectWriter
from gobjcreator2.output.ginterface_writer import GInterfaceWriter
from gobjcreator2.output.genum_writer import GEnumWriter
from gobjcreator2.output.gflags_writer import GFlagsWriter
from gobjcreator2.output.error_domain_writer import ErrorDomainWriter

top = GOCRecognizer().process_file("test.goc")
bird = top["demo::Bird"]

writer = GObjectWriter(bird)

writer.write_header()
print 80 * "-"
#writer.write_header_protected()
#print 80 * "-"
writer.write_source()
print 80 * "-"
#writer.write_marshaller_header()
#print 80 * "-"

flying_animal = top["demo::FlyingAnimal"]

writer = GInterfaceWriter(flying_animal)
writer.write_header()
print 80 * "-"
writer.write_source()
print 80 * "-"

writer = GEnumWriter(top["demo::AnimalCatg"])
writer.write_header()
print 80 * "-"
writer.write_source()
print 80 * "-"

writer = GFlagsWriter(top["demo::ActionFlags"])
writer.write_header()
print 80 * "-"

writer = ErrorDomainWriter(top["demo::ActionError"])
writer.write_header()
print 80 * "-"