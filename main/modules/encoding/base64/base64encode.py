from parentmodule import module


class base64encode(module): # Remove Char
    pass
    def __init__(self, ciphertext):
        super().__init__(ciphertext)
        self.runfunction = self.encode
        self.setOptions([])
        self.defaultParams = [("encode", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick


    def encode(self, quietMode):
        grouped = ""
        for c in self.ciphertext:
            grouped += "0"+(bin(ord(c))[2:])
        #Split into 6's
        index = 0
        completeGroups = len(grouped) // 6
        padding = ""
        if(len(grouped) % 6 != 0):
            padding = "0"*(6 - len(grouped) % 6)
        EncodedText = ""
        while completeGroups > 0:
            binary = grouped[index : index + 6]
            EncodedText += self.getEncodedValue(int(binary, 2))
            completeGroups -= 1
            index += 6
        if(padding != ""):
            binary = grouped[index : index + (6-len(padding))] + padding
            EncodedText += self.getEncodedValue(int(binary, 2))
            EncodedText += "="*(len(padding) // 2) #as 2 or 4
        if(quietMode == False):
            print(EncodedText)
        self.recentSolution = EncodedText


    def getEncodedValue(self, binary):
        if(binary >= 0 and binary <= 25):
            return chr(binary + 65)
        if(binary >= 26 and binary <= 51):
            return chr(binary + 71)
        if(binary >= 52 and binary <= 61):
            return chr(binary - 4)
        if(binary == 62):
            return '+'
        if(binary == 63):
            return '/'
