from gobjcreator2.metadef.types import NULL

class Signal(object):

    def __init__(self,
                 name,
                 result = NULL):

        self.name = name
        self.internal_name = name.replace("-", "_")
        self.result = result
        self.parameters = []

    def add_parameter(self, param):

        self.parameters.append(param)
