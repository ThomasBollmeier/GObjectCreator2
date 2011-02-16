from gobjcreator2.input.reader import Reader, GOCVisitor

class Test(GOCVisitor):

    _TABSIZE = 4

    def __init__(self):

        GOCVisitor.__init__(self)
        self._indent = 0

    def _print(self, text):

        line = " " * self._indent + text
        print line

    def package_begin(self, name):

        self._print("<package name=\"%s\">" % name)
        self._indent += Test._TABSIZE

    def package_end(self, name):

        self._indent -= Test._TABSIZE
        self._print("</package>")
    
    def gobject_begin(self, name, super_class, interfaces, attrs):

        tmp = '<gobject name=\"%s\"' % name
        if super_class:
            tmp += ' super_class="%s"' % super_class
        if "abstract" in attrs:
            tmp += ' abstract ="true"'
        if "prefix" in attrs:
            tmp += ' alias="%s"' % attrs["prefix"]

        tmp += ">"
        self._print(tmp)

        self._indent += Test._TABSIZE
        for intf in interfaces:
            self._print('<implements name="%s" />' % intf)

    def gobject_end(self, name):

        self._indent -= Test._TABSIZE
        self._print("</gobject>")

    def ginterface_begin(self, name):

        self._print("<ginterface name=\"%s\">" % name)
        self._indent += Test._TABSIZE

    def ginterface_end(self, name):

        self._indent -= Test._TABSIZE
        self._print("</ginterface>")

    def gtype(self, name):

        self._print('<gtype name="%s" />' % name)

    def error_domain(self, name, codes):

        self._print('<error_domain name="%s">' % name)
        self._indent += Test._TABSIZE

        for code in codes:
            self._print('<error_code name="%s" />' % code)

        self._indent -= Test._TABSIZE
        self._print("</error_domain>")

    def enumeration(self, name, codevals):

        self._print('<enumeration name="%s">' % name)
        self._indent += Test._TABSIZE

        for code, value in codevals:
            if value is None:
                self._print('<code name="%s" />' % code)
            else:
                self._print('<code name="%s" value="%s"/>' % (code, value))

        self._indent -= Test._TABSIZE
        self._print("</enumeration>")


    def flags(self, name, codes):

        self._print('<flags name="%s">' % name)
        self._indent += Test._TABSIZE

        for code in codes:
            self._print('<flag name="%s" />' % code)

        self._indent -= Test._TABSIZE
        self._print("</flags>")

    def method_begin(self, name, attrs, result_info):

        tmp = '<method name="%s"' % name

        if "visibility" in attrs:
            tmp += ' visibility="%s"' % attrs["visibility"]
        if "scope" in attrs:
            tmp += ' scope="%s"' % attrs["scope"]
        if "inheritance" in attrs:
            tmp += ' inheritance="%s"' % attrs["inheritance"]

        if result_info:
            tmp += ' result_type="%s"' % result_info.type_info.get_name()
    
        tmp += ">"
        self._print(tmp)
        self._indent += Test._TABSIZE

    def method_end(self, name):

        self._indent -= Test._TABSIZE
        self._print("</method>")

    def constructor_begin(self):

        self._print("<constructor>")
        self._indent += Test._TABSIZE

    def constructor_end(self):

        self._indent -= Test._TABSIZE
        self._print("</constructor>")

    def signal(self, name, result_type, args):

        tmp = '<signal name="%s" result_type="%s">' % (name, result_type)
        self._print(tmp)

        self._indent += Test._TABSIZE

        for name, type in args:
            self._print('<parameter name="%s" type="%s" />' % (name, type))

        self._indent -= Test._TABSIZE

        self._print("</signal>")

    def override(self, name):

        self._print('<override method_name="%s" />' % name)

    def parameter(self, parameter):

        tmp = '<parameter name="%s" type="%s"' % \
              (parameter.name, parameter.type_info.get_name())
        try:
            bind_to = parameter.bind_to
            if bind_to:
                tmp += ' bind_property="%s"' % bind_to
        except:
            pass
        tmp += "/>"
        self._print(tmp)

    def attribute(self, name, type_info, attrs):

        tmp = '<attribute name="%s" type="%s"' % (name, type_info.get_name())

        if "scope" in attrs:
            tmp += ' scope="%s"' % attrs["scope"]

        if "visibility" in attrs:
            tmp += ' visi="%s"' % attrs["visibility"]

        tmp += "/>"

        self._print(tmp)

    def property(self, name, attrs):

        self._print('<property name="%s">' % name)
        self._indent += Test._TABSIZE

        try:
            val = attrs["type"]
            self._print('<type>%s</type>' % val)
        except KeyError:
            pass

        try:
            val = attrs["gtype"]
            self._print('<gtype>%s</gtype>' % val)
        except KeyError:
            pass

        try:
            val = attrs["access"]
            self._print('<access>%s</access>' % val)
        except KeyError:
            pass

        try:
            val = attrs["description"].strip("\"")
            self._print('<desc>%s</desc>' % val)
        except KeyError:
            pass

        try:
            val = attrs["min"]
            self._print('<min>%s</min>' % val)
        except KeyError:
            pass

        try:
            val = attrs["max"]
            self._print('<max>%s</max>' % val)
        except KeyError:
            pass

        try:
            val = attrs["default"]
            self._print('<default>%s</default>' % val)
        except KeyError:
            pass

        self._indent -= Test._TABSIZE
        self._print('</property>')

reader = Reader()

reader.read_file("test.goc")
reader.walk_syntax_tree(Test())
