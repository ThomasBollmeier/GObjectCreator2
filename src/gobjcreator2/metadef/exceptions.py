class DefinitionError(Exception):

    def __init__(self, error_message=""):

        self.error_message = error_message

    def __str__(self):

        if self.error_message:
            message = self.error_message
        else:
            message = "A meta definition error has occurred"

        return message