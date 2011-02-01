from gobjcreator2.metadef.package import Package
from gobjcreator2.metadef.gclass import GClass
from gobjcreator2.metadef.ginterface import GInterface
from gobjcreator2.metadef.method import Method
from gobjcreator2.metadef.enums import MethodInheritance
from gobjcreator2.metadef.signal import Signal

named_object = GInterface("NamedObject", package=Package("util"))
named_object.add_method(Method("get_name"))

root = Package("bollmeier", package=Package("com"))

person = GClass("Person", package=root)
person.implement(named_object)
person.add_method(Method("is_married", inheritance_mode=MethodInheritance.VIRTUAL))

employee = GClass("Employee", super_class=person)
employee.add_method(Method("promote"))
employee.override("is_married")
employee.add_signal(Signal("last-name-changed"))

print employee.lookup_method("get_name")
print employee.lookup_method("is_married")
print employee.lookup_method('promote')
print employee._signals