from gobjcreator2.input.reader import GOCVisitor, RefTypeInfo, \
    ListTypeInfo, ConstructorParamInfo
from gobjcreator2.metadef.package import Package
from gobjcreator2.metadef.gobject import GObject
from gobjcreator2.metadef.ginterface import GInterface
from gobjcreator2.metadef.gtype import GType
from gobjcreator2.metadef.error_domain import ErrorDomain
from gobjcreator2.metadef.genum import GEnum
from gobjcreator2.metadef.gflags import GFlags
from gobjcreator2.metadef.exceptions import DefinitionError
from gobjcreator2.metadef.method import Method
from gobjcreator2.metadef.signal import Signal
from gobjcreator2.metadef.constructor import Constructor
from gobjcreator2.metadef.constants import Scope, Visibility, \
    MethodInheritance, TypeModifier
from gobjcreator2.metadef.types import *
from gobjcreator2.metadef.parameter import Parameter, ConstructorParameter
from gobjcreator2.metadef.attribute import Attribute
from gobjcreator2.metadef.property import Property, PropType, \
    PropAccess, PropGTypeValue, PropValue

class VisitorStep1(GOCVisitor):

    def __init__(self):

        GOCVisitor.__init__(self)
        self._package_stack = []

    def _get_package(self):

        if self._package_stack:
            return self._package_stack[-1]
        else:
            return None
        
    def package_begin(self, name):

        package = Package(name, package = self._get_package())
        self._package_stack.append(package)

    def package_end(self, name):

        self._package_stack.pop()

    def gobject_begin(self,
                      name,
                      super,
                      interfaces,
                      attrs):

        GObject(name, package = self._get_package())

    def ginterface_begin(self, name, attrs):

        GInterface(name, package = self._get_package())

    def gtype(self, name):

        GType(name, package = self._get_package())

    def error_domain(self, name, codes):

        ErrorDomain(name, package = self._get_package())

    def enumeration(self, name, codevals):

        GEnum(name, package = self._get_package())

    def flags(self, name, codes):

        GFlags(name, package = self._get_package())

class VisitorStep2(GOCVisitor):

    def __init__(self):

        GOCVisitor.__init__(self)
        self._stack = []

        # Mappings:

        self._scope = {
            "static": Scope.STATIC,
            "instance": Scope.INSTANCE
        }

        self._visi = {
            "public": Visibility.PUBLIC,
            "protected": Visibility.PROTECTED,
            "private": Visibility.PRIVATE
        }

        self._inheritance = {
            "final": MethodInheritance.FINAL,
            "virtual": MethodInheritance.VIRTUAL,
            "abstract": MethodInheritance.ABSTRACT
        }

        self._modifier = {
            "const": TypeModifier.CONST
        }

        self._simple_types = {
            "integer": INT,
            "unsigned integer": UNSIGNED_INT,
            "long": LONG,
            "unsigned long": UNSIGNED_LONG,
            "boolean": BOOL,
            "string": STRING,
            "float": FLOAT,
            "double": DOUBLE,
            "pointer": POINTER
        }

        self._prop_types = {
            "boolean": PropType.BOOLEAN,
            "integer": PropType.INTEGER,
            "float": PropType.FLOAT,
            "double": PropType.DOUBLE,
            "string": PropType.STRING,
            "pointer": PropType.POINTER,
            "object": PropType.OBJECT,
            "enumeration": PropType.ENUMERATION
        }

        self._prop_access = {
            "read-only": PropAccess.READ_ONLY,
            "initial-write": PropAccess.INITIAL_WRITE,
            "read-write": PropAccess.READ_WRITE
        }

    def _get_parent(self, cls):

        idx = len(self._stack) - 1

        while idx >= 0:
            parent = self._stack[idx]
            if isinstance(parent, cls):
                return parent
            else:
                idx -= 1

        if not cls == Package:
            return None
        else:
            return Package.get_top()

    def _get_param_type(self, type_info):

        if isinstance(type_info, RefTypeInfo):
            return RefType(self._get_param_type(type_info.get_ref_type()))
        elif isinstance(type_info, ListTypeInfo):
            return ListType(self._get_param_type(type_info.get_line_type()))
        else:
            type_name = type_info.get_name()
            if type_name in self._simple_types:
                return self._simple_types[type_name]
            else:
                package = self._get_parent(Package)
                return package[type_name]

    def _get_param_modifiers(self, modifiers):

        res = []
        for modifier in modifiers:
            res.append(self._modifier[modifier])

        return res

    def package_begin(self, name):

        parent = self._get_parent(Package)
        self._stack.append(parent[name])

    def package_end(self, name):

        self._stack.pop()

    def gobject_begin(self,
                      name,
                      super,
                      interfaces,
                      attrs):

        package = self._get_parent(Package)
        cls = package[name]

        if super:
            cls.set_super_class(package[super])

        for interface in interfaces:
            intf = package[interface]
            cls.implement(intf)

        for attr in attrs:
            if attr == "abstract":
                cls.abstract = attrs[attr]
            elif attr == "prefix":
                cls.prefix = attrs[attr]

        self._stack.append(cls)

    def gobject_end(self, name):

        self._stack.pop()

    def ginterface_begin(self, name, attrs):

        package = self._get_parent(Package)
        intf = package[name]

        for attr in attrs:
            if attr == "prefix":
                intf.prefix = attrs[attr]

        self._stack.append(intf)

    def ginterface_end(self, name):

        self._stack.pop()

    def gtype(self, name):

        pass

    def error_domain(self, name, codes):

        package = self._get_parent(Package)
        error_domain = package[name]

        for code in codes:
            error_domain.add_error_code(code)

    def enumeration(self, name, codevals):

        package = self._get_parent(Package)
        enum = package[name]

        for code, value in codevals:
            enum.add_code(code, value)

    def flags(self, name, codes):

        package = self._get_parent(Package)
        flags = package[name]

        for code in codes:
            flags.add_code(code)

    def method_begin(self,
                     name,
                     attrs,
                     result_info
                    ):

        cls = self._get_parent(GObject)
        if cls is None:
            intf = self._get_parent(GInterface)
        else:
            intf = None

        if cls is None and intf is None:
            error_msg = "Method %s must be defined inside gobject or ginterface"
            raise DefinitionError(error_msg)

        if result_info is not None:
            result = self._get_param_type(result_info.type_info)
            result_modifiers = self._get_param_modifiers(result_info.modifiers)
        else:
            result = NULL
            result_modifiers = []

        if cls:

            method = Method(name, result, result_modifiers)
            method.scope = Scope.INSTANCE
            method.visibility = Visibility.PRIVATE
            method.inheritance_mode = MethodInheritance.FINAL

            for attr in attrs:
                if attr == "scope":
                    method.scope = self._scope[attrs[attr]]
                elif attr == "visibility":
                    method.visibility = self._visi[attrs[attr]]
                elif attr == "inheritance":
                    method.inheritance_mode = self._inheritance[attrs[attr]]

            cls.add_method(method)

        else:

            method = Method(name, result, result_modifiers)
            method.scope = Scope.INSTANCE
            method.visibility = Visibility.PUBLIC
            method.inheritance_mode = MethodInheritance.ABSTRACT

            intf.add_method(method)

        self._stack.append(method)

    def method_end(self, name):

        self._stack.pop()

    def constructor_begin(self, prop_inits):

        cls = self._get_parent(GObject)

        constructor = Constructor(cls)

        for prop_init in prop_inits:
            value = prop_inits[prop_init]
            constructor.init_property(prop_init,
                                      value.name,
                                      value.is_codename)

        cls.constructor = constructor

        self._stack.append(constructor)

    def constructor_end(self):

        self._stack.pop()

    def signal(self, name, result_type, args):

        if result_type:
            result = self._get_param_type(result_type)
        else:
            result = NULL
        sig = Signal(name, result)

        for arg in args:
            sig.add_parameter(arg[0], self._get_param_type(arg[1]))

        cls = self._get_parent(GObject)
        if cls:
            cls.add_signal(sig)
        else:
            interface = self._get_parent(GInterface)
            interface.add_signal(sig)
        
    def override(self, name):

        pass

    def parameter(self, parameter_info):

        method = self._get_parent(Method)

        name = parameter_info.name
        type = self._get_param_type(parameter_info.type_info)
        modifiers = self._get_param_modifiers(parameter_info.modifiers)

        if not isinstance(parameter_info, ConstructorParamInfo):
            param = Parameter(name, type, modifiers)
        else:
            param = ConstructorParameter(name, type, modifiers,
                                         parameter_info.bind_to)

        method.add_parameter(param)
            
    def attribute(self,
                  name,
                  type_info,
                  attrs):

        type = self._get_param_type(type_info)

        scope = Scope.INSTANCE
        visibility = Visibility.PRIVATE
        for attr in attrs:
            if attr == "scope":
                scope = self._scope[attrs[attr]]
            elif attr == "visibility":
                visibility = self._visi[attrs[attr]]

        attribute = Attribute(name, type, scope, visibility)

        cls = self._get_parent(GObject)
        cls.add_attribute(attribute)

    def property(self,
                 name,
                 attrs):

        type = PropType.STRING
        access = PropAccess.READ_ONLY
        description = name
        gtype = None
        min_value = None
        max_value = None
        default_value = None
        auto_create = False

        for attr in attrs:

            if attr == "type":
                type = self._prop_types[attrs[attr]]
            elif attr == "access":
                access = self._prop_access[attrs[attr]]
            elif attr == "description":
                description = attrs[attr]
            elif attr == "gtype":
                value = attrs[attr]
                gtype = PropGTypeValue(value.name, value.is_typename)
            elif attr in ["min", "max", "default"]:
                value = attrs[attr]
                if attr == "min":
                    min_value = PropValue(value.name, value.is_codename)
                elif attr == "max":
                    max_value = PropValue(value.name, value.is_codename)
                elif attr == "default":
                    default_value = PropValue(value.name, value.is_codename)
            elif attr == "auto_create":
                auto_create = attrs[attr]

        prop = Property(name, type, access, description, gtype,
                        min_value, max_value, default_value, auto_create)

        cls = self._get_parent(GObject)
        cls.add_property(prop)

class VisitorStep3(GOCVisitor):

    def __init__(self):

        GOCVisitor.__init__(self)
        self._stack = []

    def _get_parent(self, cls):

        idx = len(self._stack) - 1

        while idx >= 0:
            parent = self._stack[idx]
            if isinstance(parent, cls):
                return parent
            else:
                idx -= 1

        if not cls == Package:
            return None
        else:
            return Package.get_top()

    def package_begin(self, name):

        parent = self._get_parent(Package)
        package = parent[name]

        self._stack.append(package)

    def package_end(self, name):

        self._stack.pop()

    def gobject_begin(self,
                      name,
                      super,
                      interfaces,
                      attrs):

        parent = self._get_parent(Package)
        cls = parent[name]

        self._stack.append(cls)

    def gobject_end(self, name):

        self._stack.pop()

    def override(self, name):

        cls = self._get_parent(GObject)
        cls.override(name)
