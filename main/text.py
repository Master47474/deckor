

from ttypes import types


class text():
    """
    This will be what holds the message
    The Type of the text in the message (Unicode, Hex)
    """

    def __init__(self, message, type="undefined"):
        self.types = types()
        self.message = ""
        self.type = self.types.determineType(type)

    def getMessage(self):
        return self.message

    def getType(self):
        return self.type

    #Converting To Other Types
    def setDesiredType(self, convertTo):
        """
        Sets The Type of the message to the Desired Type
        Also Converts the contents to the message to the desired Type
        Returns Boolean on Success or fail

        Modifies Current Variables of this class
        """
        return True
