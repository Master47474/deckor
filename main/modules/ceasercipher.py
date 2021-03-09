class Ceasercipher:
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext
        # Positive is anticlockwise (i.e  1 -> a = z)
        # Negative is clockwise     (i.e -1 -> a = b)
        self.shift = 0

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
