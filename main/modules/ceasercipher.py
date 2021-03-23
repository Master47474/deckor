from parentmodule import module

class ceasercipher(module):

    def __init__(self, ciphertext):
        super().__init__(ciphertext)
        self.runfunction = self.shift
        self.setOptions([["SHIFT", self.getShift,"For shift of cipher (+int anticlockwise) (-int clockwise)", self.setShift]])

        self.defaultParams = [("Shift", ["-q"], [True], [False]), ("Brute Shift", ["-q"], [True], [False])]
        #-------------------
        self.AddedCommands = [("brute", 0 , "try all 26 shifts on the ciphertext", 1)]
        self.AddedCommandsFunc = [self.bruteshift]
        self.AddedCommandsHelp = [("brute", "\t-q\t\t : for quiet mode (minimum output)")]
        self.checkargsFunc = self.checkargs
        #Module Spefic Variables
        self.shiftVal = 0


    def checkargs(self, args, validInput, result, default):
        """
        If arg is in valid input then get the resulting result
        if arg is not passed then go to default for that arg
        ORDER MATTERS
        """
        # Default unless otherwise Changes
        print("CHECKIN")
        ParameterUsed = default[:]
        i = 0
        flagsUsed = 0
        while(i < len(args)):
            if(validInput[i] in args):
                ParameterUsed[i] = result[i]
                #make 2 for when we take argment for an flag
                flagsUsed += 1
            i += 1
        Errormsg = []
        if(flagsUsed != len(args)):
            print('Fuck Error')
            for arg in args:
                if arg not in validInput:
                    Errormsg.append(arg)
            print("The Following Args Are not recoknised : ", Errormsg)
            print("Function running with default commands")
            return default
        else:
            return ParameterUsed

    # Positive is anticlockwise (i.e  1 -> a = z)
    # Negative is clockwise     (i.e -1 -> a = b)
    def shift(self, quietMode):
        print("IN SHIFT")
        print("QUIETMODE " , quietMode)
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
        return shifted


    def getShift(self):
        return self.shiftVal

    def setShift(self, shift, quietMode):
        #try:
        shift = int(shift)
        self.shiftVal = shift
        if(quietMode == False):
            print("Successfully set value of SHIFT ->", shift)
        #except:
        #    print("Please Use an int for a value\n")


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
