class Signal(object):

    def __init__(self,
                 name,
                 result):

        self.name = name
        self.internal_name = name.replace("-", "_")
        self.result = result
        self.parameters = []

    def add_parameter(self, name, type):

        self.parameters.append((name, type))
