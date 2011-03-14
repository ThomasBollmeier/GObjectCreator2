from gobjcreator2.input.reader import Reader
from gobjcreator2.input.goc_visitor import VisitorStep1, VisitorStep2, VisitorStep3
from gobjcreator2.metadef.package import Package

class GOCRecognizer(object):

    def __init__(self):

        self._reader = Reader()

    def add_include_path(self, path):

        self._reader.add_include_path(path)

    def process_file(self, file_name):

        self._reader.read_file(file_name)
        self._reader.set_main_goc_file(file_name)
        
        self._reader.walk_syntax_tree(VisitorStep1())
        self._reader.walk_syntax_tree(VisitorStep2())
        self._reader.walk_syntax_tree(VisitorStep3())

        return Package.get_top()
