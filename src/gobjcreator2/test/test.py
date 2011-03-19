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