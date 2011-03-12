from gobjcreator2.input.goc_recognizer import GOCRecognizer
from gobjcreator2.metadef.package import Package
from gobjcreator2.output.gobject_writer import GObjectWriter
from gobjcreator2.output.ginterface_writer import GInterfaceWriter

def print_types(package, indent=0):

    for element in package._elements.values():

        print " " * indent + element.name

        if isinstance(element, Package):
            indent += 4
            print_types(element, indent)
            indent -= 4

top = GOCRecognizer().process_file("test.goc")
bird = top["demo::Bird"]

writer = GObjectWriter(bird)

writer.write_header()
print 80 * "-"
#writer.write_header_protected()
#print 80 * "-"
#writer.write_source()
#print 80 * "-"
#writer.write_marshaller_header()
#print 80 * "-"

flying_animal = top["demo::FlyingAnimal"]

writer = GInterfaceWriter(flying_animal)
writer.write_header()
print 80 * "-"
writer.write_source()
