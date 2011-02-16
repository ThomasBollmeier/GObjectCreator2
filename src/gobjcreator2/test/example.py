from gobjcreator2.metadef.package import Package
from gobjcreator2.metadef.gobject import GObject
from gobjcreator2.metadef.ginterface import GInterface
from gobjcreator2.metadef.method import Method, InterfaceMethod
from gobjcreator2.metadef.parameter import Parameter
from gobjcreator2.metadef.enums import MethodInheritance, TypeModifier
from gobjcreator2.metadef.signal import Signal
from gobjcreator2.metadef.types import String

def print_method(method):

    tmp = ""

    if TypeModifier.CONST in method.result_modifiers:
        tmp += "const "

    tmp += method.result.get_name() + "\n"
    tmp += method.name + "("

    args = ""
    for p in method.parameters:
        if args:
            args += ","
        args += "\n\t%s %s" % (p.type.get_name(), p.name)
    tmp += args + ");\n"

    print tmp

named_object = GInterface("NamedObject", package=Package("util"))

m = InterfaceMethod("get_name", String(), [ TypeModifier.CONST ])
named_object.add_method(m)

root = Package("bollmeier", package=Package("com"))

person = GObject("Person", package=root)
person.implement(named_object)
person.add_method(Method("is_married", inheritance_mode=MethodInheritance.VIRTUAL))

employee = GObject("Employee", super_class=person)

salary_group = GObject("SalaryGroup")

m = Method("promote")
m.add_parameter(Parameter("salary_group", salary_group))
employee.add_method(m)

employee.override("is_married")
employee.add_signal(Signal("last-name-changed"))

print_method(employee.lookup_method("get_name").method)
print_method(employee.lookup_method("promote").method)

