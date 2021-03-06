
from text import text

class module:
    def __init__(self, ciphertext):
        #For the Parents Modules Own use
        self.ciphertext = ciphertext        #Ciphertext 'og' of time of loaded
        self.recentSolutionList = False
        self.recentSolution = None
        self.workingWithType = "undefined"  # Must be set in child
        self.replaceCipherText = False      # For Converts
        #MUST HAVE EVEN IF NOT USING IT
        #---------------------------------
        self.newtext = ""                   #the text after the runfunction is applied, only stores latestrun
        self.alteredtext = []               #Not sure
        self.alteredtextHistory = []        #
        self.options = []                   #of format (Name, self.getvaluefunc, Desc, self.variableSetterfunc)
                                            # ->>>>>BASICALLY FOR RUN TO FUNCTION WITHOUT ERROR
        self.savedSettings = []             #copy of all Values in options
        #------------------------------------------------------
        #For the Child to declare MUST!
        self.runfunction = None
        self.quick = False # To implement For a quick function
        self.defaultParams = []
        self.messageContexts = []
        #This is for extra commands that can only be used in this module
        self.AddedCommands = []              #of format ("name", index to functions list, "Desc", "index to default params")
        self.AddedCommandsFunc = []          #of format (self.func)
        self.AddedCommandsHelp = []          #of format ("name", "\tCommand\t\t : tooltip")
        self.checkargsFunc = self.checkargs
        #Modue Specific varaibles
        #For Quick
        #Goes Here

    def newText(self, contents, type):
        self.recentSolutionList = False
        self.recentSolution = text(contents, type)

    #List Version
    def newTexts(self, contents, type):
        self.recentSolutionList = True
        self.recentSolution = []
        for content in contents:
            self.recentSolution.append(text(content, type))

    def newListOfTexts(self, texts):
        self.recentSolutionList = True
        self.recentSolution = []
        for content in texts:
            self.recentSolution.append(content)

    def getRecentOutput(self):
        return self.recentSolution, self.recentSolutionList

    def checkargs(self, args, validInput, result, default):
        """
        If arg is in valid input then get the resulting result
        if arg is not passed then go to default for that arg
        ORDER MATTERS
        """
        # Default unless otherwise Changes
        ParameterUsed = default[:]
        i = 0
        flagsUsed = 0
        while(i < len(validInput)):
            if(isinstance(validInput[i], list)):
                j = 0
                while(j < len(validInput[i])):
                    if(validInput[i][j] in args):
                        ParameterUsed[i] = result[i][j]
                        #make 2 for when we take argment for an flag
                        flagsUsed += 1
                        break #as there can only be one of this type of flag hence it being in a list of a list
                    j+= 1
            else:
                if(validInput[i] in args):
                    ParameterUsed[i] = result[i]
                    #make 2 for when we take argment for an flag
                    flagsUsed += 1
            i += 1
        Errormsg = []
        if(flagsUsed != len(args)):
            print('Error With Flags')
            for arg in args:
                if arg not in validInput:
                    Errormsg.append(arg)
            print("The Following Args Are not recoknised : ", Errormsg)
            print("Function running with default commands")
            return default
        else:
            return ParameterUsed

    def callAddedFunc(self, commandIndex, paramsIndex, args):
        if(self.processsContext(False, True) == False):
            return (False, self.replaceCipherText)
        newargs = self.checkargsFunc(args, *(self.defaultParams[paramsIndex][1:]))
        self.AddedCommandsFunc[commandIndex](*newargs)
        return (True, self.replaceCipherText)

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
                setFunc(setValue, False) #all set functions of form value, QuietMode
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
        if(self.processsContext(False, True) == False):
            return (False, self.replaceCipherText)
        newargs = self.checkargsFunc(args, *(self.defaultParams[0][1:]))
        self.runfunction(*newargs)
        print("Runs recent Sol : ", self.recentSolution)
        print(self.replaceCipherText)
        return (True, self.replaceCipherText)

    def inGoodContext(self):
        if(self.ciphertext.isOfType(self.messageContexts)):
            return True
        return False

    def processsContext(self, quietMode, toConvert=False):
        if(self.inGoodContext() == False):
            if(quietMode == False):
                print("Incorrect Context of message")
                if(toConvert):
                    print("Converting")
                else:
                    print("Not Continuing with current message context")
            #Do we convert
            if(toConvert):
                #Convert it
                return True
            else:
                return False
        return True
