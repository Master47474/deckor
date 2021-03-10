from parentmodule import module

class ceasercipher(module):

    def __init__(self, ciphertext):
        super().__init__(ciphertext)
        self.runfunction = lambda : self.shift()
        self.brutefunction = lambda : self.bruteshift()
        # Positive is anticlockwise (i.e  1 -> a = z)
        # Negative is clockwise     (i.e -1 -> a = b)
        self.shiftVal = 0
        self.setOptions([["SHIFT", lambda : self.getShift(),"For shift of cipher (+int anticlockwise) (-int clockwise)", lambda x,b : self.setShift(x, b)]])


    def shift(self, quietMode=False):
        shifted = ""
        for c in self.ciphertext:
            if(c == ' '):
                shifted += c
                continue
            shifted += chr((((ord(c) - 97) -self.shiftVal) %26) +97)
        if(quietMode == False):
            if self.shiftVal > 0:
                print("Shifted by %d %s" % (self.shiftVal, "clockwise"))
            else:
                print("Shifted by %d %s" % (self.shiftVal*-1, "anticlockwise"))
        if(quietMode == False):
            self.newtext = shifted
            print(f"\n{shifted}\n")
        else:
            return shifted

    def bruteshift(self, quietMode=False):
        self.saveSettings()
        bruted = []
        for i in range(26):
            self.setShift(i, True)
            bruted.append(self.shift(True))
        self.restoreSettings()
        savetofile = self.responseNeeded("Save bruteforce to file.txt [y/n] ? ")
        printtoscreen = self.responseNeeded("Print all of bruteforce [y/n] ?")

        if(savetofile == "y"):
            print("Saved to file Check /Saves")
        if(printtoscreen == "y"):
            for i in range(26):
                print(f"{i} : {bruted[i]}")

    def getShift(self, quietMode=False):
        return self.shiftVal

    def setShift(self, shift, quietMode=False):
        #try:
        shift = int(shift)
        self.shiftVal = shift
        if(quietMode == False):
            print("Successfully set value of SHIFT ->", shift)
        #except:
        #    print("Please Use an int for a value\n")
