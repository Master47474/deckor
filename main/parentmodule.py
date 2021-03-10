class module:
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext
        self.newtext = "" #the text after the "function is applied"
        self.alteredtext = []
        self.options = [] # of type (Name, Value, Desc, variableSetter)
        self.runfunction = None
        self.brutefunction = None
        self.savedSettings = []

    def showOptions(self):
        print("\n\tName\tValue\tDescription")
        for o in self.options:
            print(f"\t{o[0]}\t{o[1]()}\t{o[2]}")
        print("")

    def responseNeeded(self, question, args=["y","n"]):
        while(True):
            answer = input(question).rstrip().lower()
            if(answer in map(lambda x : str(x).lower(), args)):
                return answer

    def appendOptions(self, element):
        self.options.append(element)

    def setOptions(self, newOptions):
        self.options = newOptions

    def getOption(self):
        return self.options

    def setOptionValue(self, setName, setValue):
        for (name, value, desc, setFunc) in self.options:
            if(setName == name):
                setFunc(setValue, False)
                break

    def resetAltered(self):
        self.alteredtext = []

    def saveSettings(self):
        #Saves the settings in options
        for op in self.options:
            self.savedSettings.append(op[1]())

    def restoreSettings(self):
        #Restores the settings in option
        for i in range(len(self.options)):
            self.options[i][3](self.savedSettings[i], True)

    def run(self):
        print("Running this Modules function")
        self.runfunction()

    def brute(self):
        print("Running this Modules brute function")
        self.brutefunction()
