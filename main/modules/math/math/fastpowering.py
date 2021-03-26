from parentmodule import module

class fastpowering(module):
    def __init__(self, ciphertext, base=1, exp=1, mod=1):
        super().__init__(ciphertext)
        self.runfunction = self.fastpower
        self.setOptions([["BASE", self.getBase, "The Base to be raised to a power", self.setBase],
                          ["EXP", self.getExp,  "The Exponent of the Base",         self.setExp],
                          ["MOD", self.getMod,  "The Modulo of the function",       self.setMod]])

        self.defaultParams = [("Fast Power", ["-q"], [True], [False])]
        #-------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Modue Specific varaibles
        try:
            self.base = int(base)
            self.exp = int(exp)
            self.mod = int(mod)
        except:
            self.base = 1
            self.exp = 1
            self.mod = 1
            print(f"One or more of the following {base},{exp},{mod} were not a valid values respictifully \n\t--setting as default")
        self.recentSolution = 1


    def fastpower(self, quietMode):
        binaryExp = bin(self.exp)
        lenStrBinExp = len(str(binaryExp)[2:])
        tempSol = 1
        for bit in range(0, lenStrBinExp):
            binaryVal = 2**bit
            basePowBVmod = (self.base**binaryVal) % self.mod
            tempSol *= basePowBVmod
            tempSol %= self.mod
        self.recentSolution = tempSol
        if(quietMode == False):
            print("The Value is = ", self.recentSolution)
        return tempSol


    def getBase(self):
        return self.base

    def getExp(self):
        return self.exp

    def getMod(self):
        return self.mod

    def setBase(self, base, quietMode):
        base = int(base)
        self.base = base
        if(quietMode == False):
            print("Successfully set value of BASE ->", base)

    def setExp(self, exp, quietMode):
        exp = int(exp)
        self.exp = exp
        if(quietMode == False):
            print("Successfully set value of EXP ->", exp)

    def setMod(self, mod, quietMode):
        mod = int(mod)
        self.mod = mod
        if(quietMode == False):
            print("Successfully set value of MOD ->", mod)
