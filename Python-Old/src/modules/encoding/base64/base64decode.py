from parentmodule import module


class base64decode(module): # Base64 Decoding
    
    def __init__(self, ciphertext):
        super().__init__(ciphertext)
        self.runfunction = self.decode
        self.setOptions([])
        self.defaultParams = [("decode", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick
        self.indextable = [chr(x+65) for x in range(26)]
        self.indextable += [chr(x+71) for x in range(26, 52)]
        self.indextable += [chr(x-4) for x in range(52, 62)]
        self.indextable += ['+', '/']

    def decode(self, quietMode):
        DecodedText = ""
        grouped = ""
        padding = 0
        for c in self.ciphertext:
            if(c == "="):
                padding += 1
                continue
            grouped += self.getDecodedValue(c)
        #remove padding from grouped
        if(padding != 0):
            grouped = grouped[:-padding*2]
        index = 0
        #Split back into 8 bits
        while( index != len(grouped)):
            DecodedText += chr(int(grouped[index : index + 8], 2))
            index += 8
        if(quietMode == False):
            print(DecodedText)
        self.recentSolution = DecodedText


    def getDecodedValue(self, char):
        #returns the index from the indextable (of type binary of size 6 bits (in string format))
        for i,c in enumerate(self.indextable):
            if c == char:
                return bin(i)[2:].zfill(6)
        return -1
