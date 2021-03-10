import os
import importlib

class Console:
    """
    Commands Type as follows
    0: ??
    """

    def __init__(self, ciphertext):
        self.originalCiphertext = ciphertext
        self.commandsType = 0
        self.modulePath = "\\"
        self.modulePathprefix = "modules\\"
        self.module = None
        self.uselist = []

    def printciphertext(self):
        print(f"\nOriginal:\n{self.printciphertext}\n")

    def awaitcommand(self):
        inline = input(f"dec ({self.modulePath}) > ")
        args = [x for x in inline.split(" ") if x != '' ]
        command = args[0]
        self.commands(command, args[1:])

    def printuselist(self):
        i = 0
        print("\n\tUse\tModule\n")
        for o in self.uselist:
            print(f"\t{i}\t{o}")
            i += 1
        print("\n")

    def resetmodule(self):
        self.modulePath = "\\"
        self.modulePathprefix = "modules\\"
        self.module = None

    def updatemodule(self, path, module):
        self.modulePath = f"\\{path}"
        self.module = module(self.originalCiphertext)

    #all commands are in all caps
    def commands(self, command, args):
        #debugging print("Args : " , args)
        if(command == "help" or command == "HELP"):
            self.help()
        elif(command.lower() == "quit"):
            exit()
        elif(command == "SEARCH"):
            self.search(args)
        elif(command == "ORIGINAL" or command == "OG"):
            self.original(args)
        elif(command == "USE"):
            self.use(args)
        elif(command == "SHOW"):
            self.show(args)
        elif(command == "UNLOAD"):
            self.unload()
        elif(command == "SET"):
            self.set(args)
        elif(command == "RUN"):
            self.run()
        elif(command == "BRUTE"):
            self.brute()
        elif(command == "FREQA"):
            self.freqa()
        else:
            print("Command not recognised")

    def help(self):
        print("\tSEARCH\t\t : Use to search for tools to use")
        print("\tORIGINAL \ OG\t\t : Shows last loaded cipher. -a to list all prev ciphers")
        print("\tUSE\t\t : Use to load a module")
        print("\tSHOW\t\t : Use to get options for a module")
        print("\nModule shit --------")
        print("\tUNLOAD\t\t : Use to unload a module and wiping any settings set for said module")
        print("\tSET\t\t : Use to set a variable in a module")
        print("\tRUN\t\t : Use to run a module")
        print("\tBRUTE\t\t : Use to run brute force variant2 a module")
        print("\tFREQA\t\t : Use for Frequency Analysis")
        print("")

    def freqa(self):
        import modules.frequencyanalysis as fa
        fa.frequencyanalysis(self.originalCiphertext)

    def search(self,args):
        modulesMatching = []
        if(args == []):
            print("Please Sepcify an term to search")
            return
        self.uselist = []
        match = args[0]
        for (root, dirs, files) in os.walk("modules"):
            for file in files:
                if(file.endswith(".py")):
                    if(match in file[0:-3]):
                        self.uselist.append(os.path.join(root, file[0:-3]))
                        #print("\t%d\t"%usei, os.path.join(root, file[0:-3]))
        if(len(self.uselist) > 0):
            self.printuselist()

    def original(self, args):
        #Have Args to see all previous loaded ciphers
        print("Orignal Last Loaded Ciphertext")

    def use(self, args):
        if(args == []):
            print("No arguments specified\n")
            if(len(self.uselist) > 0):
                print("Maybe try \'USE x\' from the list below")
                self.printuselist()
            return

        self.resetmodule()
        moduletoload = None
        try:
            moduletoload = self.uselist[int(args[0])]
            print("Loaded ", moduletoload, "Successfully\n")
        except:
            moduletoload = args[0]
            if(os.path.exists(moduletoload + ".py") and (moduletoload != "parentmodule")):
                print("Loaded", moduletoload, "Successfully\n")
            else:
                print("Couldnt Load", moduletoload, "Successfully")
                print("Does this path exist\n")
                return
        #----------------------------------------------------
        modulestr = ".".join(moduletoload.split('\\'))
        mod = importlib.import_module(modulestr)
        clas = getattr(mod, modulestr[8:])
        #create a parent class that all modules use which has the same functions that all can use??!!! FUCKKKK
        #----------------------------------------------------
        self.updatemodule(moduletoload, clas)

    def unload(self):
        if(self.module == None):
            print("No module loaded to unload\n")
            return
        self.resetmodule()

    def set(self, args):
        if(self.module == None):
            print("Please Load a Module first\n")
            return
        (name, value) = (args[0], args[1])
        self.module.setOptionValue(name, value)

    def show(self, args):
        #add logic for args
        self.options()

    def options(self):
        if (self.module == None):
            print("Please Load a Module first\n")
            return
        #from module.ceasercipher import ceasercipher
        #cc = ceasercipher("aaaa")
        self.module.showOptions()

    def run(self):
        self.module.run()

    def brute(self):
        self.module.brute()
