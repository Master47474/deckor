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
        self.module = module

    #all commands are in all caps
    def commands(self, command, args):
        #debugging print("Args : " , args)
        if(command == "help" or command == "HELP"):
            self.help()
        elif(command.lower() == "quit"):
            exit()
        elif(command == "FREQA"):
            self.freqa()
        elif(command == "SEARCH"):
            self.search(args)
        elif(command == "USE"):
            self.use(args)
        elif(command == "UNLOAD"):
            self.unload()

    def help(self):
        print("\tSEARCH\t\t : Use to search for tools to use")
        print("\tUSE\t\t : Use to load a module")
        print("\tUNLOAD\t\t : Use to unload a module and wiping any settings set for said module")
        print("\tFREQA\t\t : Use for Frequency Analysis")

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

    def use(self, args):
        self.resetmodule()
        moduletoload = None
        try:
            moduletoload = self.uselist[int(args[0])]
            print("Loaded ", moduletoload, "Successfully\n")
        except:
            moduletoload = args[0]
            if(os.path.exists(moduletoload + ".py")):
                print("Loaded", moduletoload, "Successfully\n")
            else:
                print("Couldnt Load", moduletoload, "Successfully")
                print("Does this path exist\n")
                return
        #----------------------------------------------------
        modulestr = moduletoload.split('\\').join(".")
        mod = importlib.import_module(modulestr)
        #create a parent class that all modules use which has the same functions that all can use??!!! FUCKKKK
        #----------------------------------------------------
        self.updatemodule(moduletoload, None)

    def unload(self):
        self.resetmodule()
