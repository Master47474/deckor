from parentmodule import module


class unicode(module): # undefined to unicode

    def __init__(self, ciphertext, replaceText=False):
        super().__init__(ciphertext)
        self.runfunction = self.convert
        self.setOptions([])
        self.defaultParams = [("convert", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick
        self.replaceCipherText = replaceText



    """
    Converting to unicode from undefined is as simple as just setting the type
    as python stores strings as unicode

    Should never be used unless user knows it is correct type
    """
    def convert(self, quietMode):
        self.ciphertext.setType("unicode")
