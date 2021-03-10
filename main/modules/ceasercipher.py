from parentmodule import module

class ceasercipher(module):

    def __init__(self, ciphertext):
        super().__init__(ciphertext)
        # Positive is anticlockwise (i.e  1 -> a = z)
        # Negative is clockwise     (i.e -1 -> a = b)
        self.shift = 0
        self.setOptions([["SHIFT", lambda : self.getShift(),"For shift of cipher (+int anticlockwise) (-int clockwise)", lambda x : self.setShift(x)]])



    def shift(self):
        shifted = ""
        for c in self.ciphertext:
            if(c == ' '):
                shifted += c
                continue
            shifted += chr( (((ord(c) - 97) - self.shift ) % 26) + 97 )
        if self.shift > 0:
            print("Shifted by %d %s", self.shift, "clockwise" )
        else:
            print("Shifted by %d %s", self.shift*-1, "anticlockwise" )


    def getShift(self):
        return self.shift

    def setShift(self, shift):
        #try:
        shift = int(shift)
        self.shift = shift
        #except:
        #    print("Please Use an int for a value\n")
