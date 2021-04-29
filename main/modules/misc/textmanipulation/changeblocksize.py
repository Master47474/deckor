from parentmodule import module

class changeblocksize(module): # Remove Char
    pass
    def __init__(self, ciphertext, size=None, inspace=False):
        super().__init__(ciphertext)
        self.runfunction = self.splitIntoBlock
        self.setOptions([["SIZE", self.getSize,"Size of each block", self.setSize],
                         ["INSPACE", self.getInSpace,"Include Space with blocks (Set False Auto)", self.setInSpace]])
        self.defaultParams = [("Split Block Size", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick
        try:
            self.size = int(size)
            if((inspace.lower() == "false" or inspace.lower() == "true") == 0):
                self.inspace = (False, True)[inspace.lower() == "true"]
            else:
                raise IndexError
        except:
            #Size of 0 implies inf block size
            self.size = 0
            self.inspace = False
            print(f"the following {size},{inspace} were not a valid value for SIZE, INSPACE respictifully \n\t--setting as default")

    def splitIntoBlock(self, quietMode):
        if(self.size == 0):
            self.recentSolution = self.ciphertext
            return

        newText = ""
        i = 0
        for c in self.ciphertext:
            if(c == " " and self.inspace == False):
                continue
            newText += c
            i += 1
            if((i%self.size) == 0):
                newText += " "
        self.recentSolution = newText

    #Setters and Getters
    def setSize(self, size, quietMode):
        self.size = int(size)
        if(quietMode == False):
            print("Successfully set value of SIZE ->", self.size)

    def getSize(self):
        return self.size


    def setInSpace(self, inspace, quietMode):
        if((inspace.lower() == "false" or inspace.lower() == "true") == 0):
            self.inspace = (False, True)[inspace.lower() == "true"]
        if(quietMode == False):
            print("Successfully set value of INSPACE ->", self.inspace)

    def getInSpace(self):
        return self.inspace
