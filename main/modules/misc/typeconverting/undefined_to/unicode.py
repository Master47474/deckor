from parentmodule import module


class unicode(module): # undefined to unicode

    def __init__(self, ciphertext, replaceText=False):
        super().__init__(ciphertext)
        self.runfunction = self.convert
        self.setOptions([["REPLACE", self.getReplace, "For Replacing the ciphertext in the main console after running main run command", self.setReplace]])
        self.replaceCipherText = replaceText

        self.defaultParams = [("convert", ["-q"], [True], [False])]
        self.messageContexts = ["void"]
        #-------------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick

    """
    Converting to unicode from undefined is as simple as just setting the type
    as python stores strings as unicode

    Should never be used unless user knows it is correct type
    And For Testing new Params LMAO
    """
    def convert(self, quietMode):
        self.newText(self.ciphertext.getMessage(), "unicode")

    def getReplace(self):
        return self.replaceCipherText

    def setReplace(self, newValue, quietMode):
        if(newValue.lower() == "true"):
            self.replaceCipherText = True
            if(quietMode == False):
                print("Succesfull Setting of new value")
            return
        if(newValue.lower() == "false"):
            self.replaceCipherText = False
            if(quietMode == False):
                print("Succesfull Setting of new value")
            return
        if(quietMode == False):
            print("Unable to set new Value of REPALCE")
