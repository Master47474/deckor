from parentmodule import module

class replacechar(module): # Remove Char
    pass
    def __init__(self, ciphertext, targetChar=None, removeChar=None):
        super().__init__(ciphertext)
        self.runfunction = self.replaceChar
        self.setOptions([["TARGET", self.getTargetChar,"Char that will be replaced by REPLACE", self.setTargetChar],
                         ["REPLACE", self.getReplaceChar, "Char that will replace TARGET (DEFAULT NULL CHAR)", self.setReplaceChar]])
        self.defaultParams = [("ReplaceChar", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick
        try:
            if(self.targetChar == None or self.replaceChar == None):
                raise
            self.targetChar = "\'"+str(targetChar)+"\'"
            self.replaceChar = "\'"+str(removeChar)+"\'"
        except:
            self.targetChar = "\'\'"
            self.replaceChar = "\'\'"
            print(f"One or more of the following {targetChar},{removeChar} were not a valid values respictifully \n\t--setting as default")

    def replaceChar(self, quietMode):
        newText = ""
        target = self.targetChar[1:-1]
        replaced = self.replaceChar[1:-1]
        for i in range(len(self.ciphertext)):
            newText += (self.ciphertext[i], replaced)[self.ciphertext[i] == target]
        self.recentSolution = newText

    #Setters and Getters
    def setTargetChar(self, char, quietMode):
        self.targetChar = "\'"+char[1:-1]+"\'"
        if(quietMode == False):
            print("Successfully set value of TARGET ->", self.targetChar)

    def getTargetChar(self):
        return self.targetChar

    def setReplaceChar(self, char, quietMode):
        self.replaceChar = "\'"+char[1:-1]+"\'"
        if(quietMode == False):
            print("Successfully set value of REPLACE ->", self.replaceChar)

    def getReplaceChar(self):
        return self.replaceChar
