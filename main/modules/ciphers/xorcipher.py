from parentmodule import module

class xorcipher(module):
    def __init__(self, ciphertext, key=None, keyType=None ,textToXor=None, textType=None):
        super().__init__(ciphertext)
        self.runfunction = self.XOR
        self.setOptions([["KEY", self.getKey, "The Key for the cipher", self.setKey],
                         ["MESSAGE", self.getMessage, "The Key for the cipher", self.setMessage],
                         ["KT", self.getKeyType, "Type of the key", self.setKeyType],
                         ["MT", self.getMessageType, "Type of the message", self.setMessageType]])

        self.defaultParams = [("XOR", ["-q"], [True], [False])]
        #-------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Module Specfic Variables
        #For Quick
        if(textToXor == None):
            self.textToXor = ciphertext
        else:
            self.textToXor = textToXor
        try:
            self.key = str(key)
            if(len(self.key) < len(self.textToXor)):
                IntentinalError = int("a")
        except:
            self.key = "A"*len(self.textToXor)
            print(f"One or more of the following {key},{textToXor} were not a valid values respictifully \n\t--setting as default")
        self.messageType = "unicode"
        self.keyType = "unicode"

    def XOR(self, quietMode):
        if self.messageType == "unicode" && self.keyType == "unicode":
            self.recentSolution = self.uuXORb(quietMode)
            print("Completed")
            return


    #types of Xors
    #all outptus are of type Bytes, Mainuplation of output  MUST bed one after the function
    #in python3 all Strings are of Type unicode

    #Input of Key: unicode textToXor: unicode
    #Ouput of xored : bytes
    def uuXORb(self, quietMode) -> bytes:
        #convert key and string from unicode to bytes
        bytes_key = self.key.encode()
        bytes_textToXor = self.textToXor.encode()
        xoredText = []
        for i in range(len(bytes_textToXor)):
            xoredText.append(bytes_key[i] ^ bytes_textToXor[i])
        if(quietMode == False):
            print("Bytes are ", bytes(xoredText))
            print("In Readable hex ", " ".join([(hex(x)[2:].zfill(2)).upper() for x in xoredText]))
        return bytes(xoredText)





    #Setters and Getters
    def setKey(self, newKey, quietMode):
        if(len(newKey) < len(self.textToXor)):
            print("Did not Successfully set value of KEY ->", newKey, "as length is less than message, set message first")
            return
        self.key = newKey
        if(quietMode == False):
            print("Successfully set value of KEY ->", newKey)

    def getKey(self):
        return self.key

    def setMessage(self, Message, quietMode):
        if(len(self.key) < len(Message)):
            print("Did not Successfully set value of MESSAGE ->", Message, "as length is less than message")
            return
        self.textToXor = Message
        if(quietMode == False):
            print("Successfully set value of MESSAGE ->", Message)

    def getMessage(self):
        return self.textToXor


    def setKeyType(self, keyType, quietMode):
        self.keyType = keyType
        if(quietMode == False):
            print("Successfully set value of KT ->", keyType)

    def getKeyType(self):
        return self.keyType

    def setMessageType(self, messageType, quietMode):
        self.messageType = messageType
        if(quietMode == False):
            print("Successfully set value of MT ->", messageType)

    def getMessageType(self):
        return self.messageType
