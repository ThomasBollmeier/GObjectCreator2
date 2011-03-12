from gobjcreator2.output.writer import Writer

class GInterfaceWriter(Writer):

    def __init__(self, interface):

        Writer.__init__(self)
        
        self._intf = interface
        
    def write_header(self):
        
        pass
    
    def write_source(self):
        
        pass
