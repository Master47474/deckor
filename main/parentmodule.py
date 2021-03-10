class module:
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext
        self.options = [] # of type (Name, Value, Desc, variableSetter)

    def showOptions(self):
        print("\n\tName\tValue\tDescription")
        for o in self.options:
            print(f"\t{o[0]}\t{o[1]()}\t{o[2]}")
        print("")


    def appendOptions(self, element):
        self.options.append(element)

    def setOptions(self, newOptions):
        self.options = newOptions

    def getOption(self):
        return self.options

    def setOptionValue(self, setName, setValue):
        for (name, value, desc, setFunc) in self.options:
            if(setName == name):
                setFunc(setValue)
                break

    def run(self):
        print("Run this function")
