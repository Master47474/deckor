from parentmodule import module

class diffiehellman(module): # dffie-hellman

    def __init__(self, ciphertext, prime=None, root=None, a=None, b=None):
        super().__init__(ciphertext)
        self.runfunction = self.genereateKeys
        self.setOptions([["P", self.getP,"Size of field of size P, prime", self.setP],
                         ["G", self.getG,"Primitive Root for Field of P", self.setG],
                         ["A", self.getA,"Alice's Secret", self.setA],
                         ["B", self.getB,"Bobs' Secret", self.setB]])

        self.defaultParams = [("Genereate Keys", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick
        try:
            self.P = int(prime)  # field size
            self.G = int(root)    # primitive root for field
            self.A = int(a)                 # Alice Secret
            self.B = int(b)                 # Bob Secret
        except:
            self.P = 23  # field size
            self.G = 5    # primitive root for field
            self.A = 1              # Alice Secret
            self.B = 1              # Bob Secret
            print(f"Was not a valid value for ... \n\t--setting as default")


    """
    Implimentation of diffie-hellman will be using the following and original implimentation
    On a Multipliciative Field of integers modulo p (prime) and primitive root g
    """
    def genereateKeys(self, quietMode):
        if(quietMode == False):
            print("Using P : ", self.P)
            print("Using G : ", self.G)
            print("1st round Calculations")
        gA = (self.G ** self.A) % self.P
        gB = (self.G ** self.B) % self.P
        if(quietMode == False):
            print("Alice --> Bob : ", gA)
            print("Bob --> Alice : ", gB)
            print("Final round Calculations")
        gAB = (gA ** self.B) % self.P
        gBA = (gB ** self.A) % self.P
        self.recentSolution = gAB
        if(quietMode == False):
            print("Key determined is : ", gAB)

    #Setters And Getters
    def setP(self, newP, quietMode):
        try:
            self.P = int(newP)
            if(quietMode == False):
                print("Successfully set value of P ->", newP)
        except:
            print("Please Input a valid integer for P")

    def getP(self):
        return self.P

    def setG(self, newG, quietMode):
        try:
            self.G = int(newG)
            if(quietMode == False):
                print("Successfully set value of G ->", newG)
        except:
            print("Please Input a valid integer for G")

    def getG(self):
        return self.G

    def setA(self, newA, quietMode):
        try:
            self.A = int(newA)
            if(quietMode == False):
                print("Successfully set value of A ->", newA)
        except:
            print("Please Input a valid integer for A")

    def getA(self):
        return self.A

    def setB(self, newB, quietMode):
        try:
            self.B = int(newB)
            if(quietMode == False):
                print("Successfully set value of B ->", newB)
        except:
            print("Please Input a valid integer for B")

    def getB(self):
        return self.B
