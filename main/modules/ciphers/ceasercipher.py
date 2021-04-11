from parentmodule import module
"""
To Add for this Module

1) Save output to file

"""


class ceasercipher(module): # Shift Cipher

    def __init__(self, ciphertext, shiftVal=None):
        super().__init__(ciphertext)
        self.runfunction = self.shift
        self.setOptions([["SHIFT", self.getShift,"For shift of cipher (+int anticlockwise) (-int clockwise)", self.setShift]])

        self.defaultParams = [("Shift", ["-q"], [True], [False]), ("Brute Shift", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = [("brute", 0 , "try all 26 shifts on the ciphertext", 1)]
        self.AddedCommandsFunc = [self.bruteshift]
        self.AddedCommandsHelp = [("brute", "\t-q\t\t : for quiet mode (minimum output)")]
        #Module Specfic Variables
        #For Quick
        try:
            self.shiftVal = int(shiftVal)
        except:
            self.shiftVal = 0
            print(f"{shiftVal} was not a valid value for SHIFT \n\t--setting as default")


    # Positive is anticlockwise (i.e  1 -> a = z)
    # Negative is clockwise     (i.e -1 -> a = b)
    def shift(self, quietMode):
        shifted = ""
        for c in self.ciphertext:
            if(c == ' '):
                shifted += c
                continue
            shifted += chr((((ord(c) - 97) - self.shiftVal) %26) +97)
        if(quietMode == False):
            if self.shiftVal > 0:
                print("Shifted by %d %s" % (self.shiftVal, "clockwise"))
            else:
                print("Shifted by %d %s" % (self.shiftVal*-1, "anticlockwise"))
            self.newtext = shifted
            print(f"\n{shifted}\n")
        self.recentSolutionList = False
        self.recentSolution = shifted


    #Added Outside Commands
    #OUTSIDE COMMANDS MUST USE THE args as a paremeter and set them manually in the list self.AddedCommandsFunc(checkargs())
    def bruteshift(self, quietMode):
        """
        Parameters Useds
        BOOL quietMode
        """
        self.saveSettings()
        bruted = []
        for i in range(26):
            self.setShift(i, quietMode)
            bruted.append(self.shift(quietMode))
        self.restoreSettings()
        savetofile = self.responseNeeded("Save bruteforce to file.txt [y/n] ? ")
        printtoscreen = self.responseNeeded("Print all of bruteforce [y/n] ?")

        if(savetofile == "y"):
            print("Saved to file Check /Saves")
        if(printtoscreen == "y"):
            for i in range(26):
                print(f"{i} -{26-i} : {bruted[i]}")

        self.recentSolutionList = True
        self.recentSolution = bruted


    #Setters and Getters
    def getShift(self):
        return self.shiftVal

    def setShift(self, shift, quietMode):
        try:
            shift = int(shift)
            self.shiftVal = shift
            if(quietMode == False):
                print("Successfully set value of SHIFT ->", shift)
        except:
            print("Please Use an int for a SHIFT VALUE\n")
