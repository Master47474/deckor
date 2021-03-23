class module:
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext
        self.newtext = "" #the text after the "function is applied"
        self.alteredtext = []
        self.options = [] # of type (Name, Value, Desc, variableSetter)
        self.runfunction = None
        self.savedSettings = []
        #This is for extra commands that can only be used in this module
        # of format ("name", index to functions list, "Desc", "index to default params")
        self.AddedCommands = []
        #of format ( args : func(args))
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        self.defaultParams = []
        self.checkargsFunc = None

    def callAddedFunc(self, commandIndex, paramsIndex, args):
        newargs = self.checkargsFunc(args, *(self.defaultParams[paramsIndex][1:]))
        self.AddedCommandsFunc[commandIndex](*newargs)

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

    def printExtraCommands(self):
        print("The Modules Extra Commands ------")
        if (self.AddedCommands == []) :
            print("There are no Added Commands for this module\n")
            return
        for(command, index, desc, idp) in self.AddedCommands:
            print("\t%s\t\t : %s" % (command, desc))

    def printExtraCommandsHelp(self, com):
        print("Command Arguments ------")
        if (self.AddedCommandsHelp == []) :
            print("There are no Commands flags for this command\n")
            return
        for(command, desc) in self.AddedCommandsHelp:
            if(command == com):
                print("\t%s\t\t : %s" % (command, desc))

    def run(self, args):
        print("Running this Modules Main function")
        print("args: ", args)
        print("Default params : ", self.defaultParams[0][1:])
        newargs = self.checkargsFunc(args, *(self.defaultParams[0][1:]))
        print(newargs)
        self.runfunction(*newargs)
