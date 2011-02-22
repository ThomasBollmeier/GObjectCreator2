import gobjcreator2.metadef.types as types
from gobjcreator2.metadef.gobject import GObject
from gobjcreator2.metadef.ginterface import GInterface
from gobjcreator2.metadef.package import PackageElement

class Output(object):

    def wrt(self, text, line_break):

        pass

class StdOut(Output):

    def wrt(self, text, line_break):

        if line_break:
            print text
        else:
            print text,

class Writer(object):

    def __init__(self):

        self._indent = 0
        self._tab_size = 4
        self._output = StdOut()

    def set_output(self, output):

        self._output = output

    def set_tab_size(self, size):

        self._tab_size = size

    def write(self, text):

        tmp = " " * self._indent + text
        self._output.wrt(tmp, line_break=False)

    def writeln(self, text=""):

        tmp = " " * self._indent + text
        self._output.wrt(tmp, line_break=True)

    def user_section(self, name):

        self.writeln("/* UserCode %s { */" % name)
        self.writeln()
        self.writeln("/* } UserCode */")

    def indent(self):

        self._indent += self._tab_size

    def unindent(self):

        self._indent -= self._tab_size

    def typename(self, type):

        if isinstance(type, types.RefType):
            res = self.typename(type.ref_type) + "*"
        elif isinstance(type, types.ListType):
            res = self.typename(type.line_type) + "*"
        elif type is types.BOOL:
            res = "gboolean"
        elif type is types.INT:
            res = "gint"
        elif type is types.UNSIGNED_INT:
            res = "guint"
        elif type is types.LONG:
            res = "glong"
        elif type is types.UNSIGNED_LONG:
            res = "gulong"
        elif type is types.FLOAT:
            res = "gfloat"
        elif type is types.DOUBLE:
            res = "gdouble"
        elif type is types.STRING:
            res = "gchar*"
        elif type is types.POINTER:
            res = "gpointer"
        elif type is types.NULL:
            res = "void"
        elif isinstance(type, PackageElement):
            res = type.name
            p = type.package
            while p:
                if p.name:
                    res = p.name.capitalize() + res
                p = p.package
            if isinstance(type, GObject) or isinstance(type, GInterface):
                res += "*"

        return res
