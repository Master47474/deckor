import os

class Console:
    """
    Commands Type as follows
    0: ??
    """

    def __init__(self, ciphertext):
        self.originalCiphertext = ciphertext
        self.commandsType = 0
        self.modulePath = "/"
        self.modulePathprefix = "modules/"
        self.module = None

    def printciphertext(self):
        print(f"\nOriginal:\n{self.printciphertext}\n")

    def awaitcommand(self):
        inline = input(f"dec ({self.modulePath}) > ")
        args = [x for x in inline.split(" ") if x != '' ]
        command = args[0]
        self.commands(command, args[1:])



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

    def help(self):
        print("\tSEARCH\t\t : Use to search for tools to use")
        print("\tFREQA\t\t : Use for Frequency Analysis")

    def freqa(self):
        import modules.frequencyanalysis as fa
        fa.frequencyanalysis(self.originalCiphertext)

    def search(self,args):
        modulesMatching = []
        if(args == []):
            print("Please Sepcify an term to search")
            return
        match = args[0]
        print("\n")
        for (root, dirs, files) in os.walk("modules"):
            for file in files:
                if(file.endswith(".py")):
                    if(match in file[0:-3]):
                        print("\t", os.path.join(root, file[0:-3]))
        print("\n")
