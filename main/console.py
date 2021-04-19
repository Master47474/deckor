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
        self.cwd = os.getcwd()  #Current Working Dir
        print("cwd = ",self.cwd)
        #contents , module that returned it
        self.resultlist = []
        self.invokedResult = None
        self.uselist = []
        #of form (command , points to index in commandsFunc) as multiple commands can point to same function
        self.commandsList = [("help", 0), ("quit", 1), ("search", 2), ("original", 3), ("og", 3), ("show", 4), ("unload", 5),
                             ("set", 6), ("run", 7), ("use", 8), ("uselist", 9), ("ul", 9), ("quick", 10), ("res", 11),
                             ("resultslist", 12), ("rl", 12), ("fload", 13), ("cd", 14), ("pwd", 15), ("ls", 16)]
        #all take the args argument but some dont use it
        self.commandsFunc = [self.help, self.quit, self.search, self.original, self.show, self.unload,
                             self.set, self.run, self.use, self.showUseList, self.quick, self.res, self.showResultsList,
                             self.fload, self.cd, self.pwd, self.ls]


    #def returnfunc(self, )
    def printciphertext(self):
        print(f"\nOriginal:\n{self.originalCiphertext}\n")

    def awaitcommand(self):
        inline = input(f"dec ({self.modulePath}) > ")
        args = [x for x in inline.split(" ") if x != '' ]
        command = args[0]
        print("args " , args[1:])
        self.commands(command, args[1:])

    def printuselist(self):
        i = 0
        print("\n\tUse\tModule\n")
        for o in self.uselist:
            print(f"\t{i}\t{o}")
            i += 1
        print("\n")

    def printresultlist(self):
        i = 0
        print("\n\tResult\tContents\tModule\n")
        for o, m in self.resultlist:
            print(f"\t{i}\t{o}\t\t{m}")
            i += 1
        print("\n")

    def setInvokeResult(self, result):
        self.invokedResult = result[0]

    def pushResult(self, result, moduleStr):
        self.resultlist.append((result, moduleStr))

    def reorderArgs(self, keyword, argsNo, args):
        #argsNo is useless rightnow
        newargs = args[:]
        deletedIndcies = []
        try:
            for i in range(len(args)):
                if(args[i] == keyword):
                    if(args[i] == "res"):
                        self.res(args[i+1])
                        deletedIndcies.append(i+1)
                        newargs[i] = self.invokedResult
                        continue
            offset = 0
            for di in deletedIndcies:
                del newargs[di - offset]
                offset += 1
        except:
            print("Error Invoking Res x")
        return newargs

    def resetmodule(self):
        self.modulePath = "\\"
        self.modulePathprefix = "modules\\"
        self.module = None

    def updatemodule(self, path, module, quickArgs=[]):
        self.modulePath = f"\\{path}"
        if(quickArgs == []):
            self.module = module(self.originalCiphertext)
        else:
            try:
                self.module = module(self.originalCiphertext, *quickArgs)
            except:
                print("Error with setting args for module ... resetting")
                self.resetmodule()

    def setModule(self, path, module):
        self.modulePath = path
        self.module = module

    #all commands are in all caps
    def commands(self, command, args):
        #debugging print("Args : " , args)
        #reword args is res keyword is used
        args = self.reorderArgs("res", 1, args)
        print("new Args ", args)
        for (com, index) in self.commandsList:
            if(command == com):
                if(len(args) >  0):
                    if(args[0] == "?"):
                        print("extra help for command args")
                        return
                self.commandsFunc[index](args)
                return
        if(self.module != None):
            for (com, index, desc, idp) in self.module.AddedCommands:
                if(command == com):
                    if(len(args) >  0):
                        if(args[0] == "?"):
                            print("Extra Help for command args")
                            return
                    self.module.callAddedFunc(index, idp, args)
                    #self.module.AddedCommandsFunc[index](args)
                    return
        print("Command not reckognised")

    def quit(self, args):
        exit()

    def help(self, args):
        print("\tsearch\t\t : Use to search for tools to use")
        print("\toriginal \ og\t : Shows last loaded cipher. -a to list all prev ciphers")
        print("\tuse\t\t : Use to load a module")
        print("\tres\t\t : Use to invoke a recent result")
        print("\tuselist\t\t : Use to show current uselist")
        print("\tresultslist\t : Use to show recent results list")
        print("\tshow\t\t : Use to get options for a module")
        print("\tquick\t\t : Use to quickly load and execute the modules run function wihtout loading the module. Must put inpout args")
        print("\tfload\t\t : Use to load in text from a a file")
        print("\nModule shit --------")
        print("\tunload\t\t : Use to unload a module and wiping any settings set for said module")
        print("\tset\t\t : Use to set a variable in a module")
        print("\trun\t\t : Use to run a module")
        print("\nDirectory shit --------")
        print("\tpwd\t\t : Path to working directory")
        print("\tcd\t\t : Change Directory")
        print("\tls\t\t : List all files in Current working directory")
        print("")
        if(self.module != None):
            self.module.printExtraCommands()
        print("")

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
        self.printciphertext()

    def use(self, args, isQuick=False, quickArgs=[]):
        print('USE ARGS = ', args)
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
        clas = getattr(mod, moduletoload.split('\\')[-1])
        #create a parent class that all modules use which has the same functions that all can use??!!! FUCKKKK
        #----------------------------------------------------
        if(isQuick == False):
            self.updatemodule(moduletoload, clas)
        else:
            self.updatemodule(moduletoload, clas, quickArgs)

    def res(self, args):
        print('RES ARGS = ', args)
        if(args == []):
            print("No arguments specified\n")
            if(len(self.resultlist) > 0):
                print("Maybe try \'RES x\' from the list below")
                self.printresultlist()
                return
        try:
            if(int(args[0]) < len(self.resultlist)):
                self.setInvokeResult(self.resultlist[int(args[0])])
            else:
                print("Index out of range for result list")
        except:
            print("Please input a valid index")


    def showUseList(self, args):
        self.printuselist()

    def showResultsList(self, args):
        self.printresultlist()

    def unload(self, args):
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
        self.options(args)

    def quick(self, args):
        print("Quick")
        savedMod, savedPath = self.module, self.modulePath
        self.unload(args)
        self.use(args[1], True, args[2:])
        if(self.module != None):
            self.run([])
        self.unload(args)
        self.setModule(savedPath, savedMod)

    def fload(self, args):
        print("Running fload")
        #check if file is in path exists
        if(len(args) > 0):
            val, newPath = self.pathexists(args[0])
            if(val):
                print("File %s Exists" % args[0])
                with open(newPath, 'r') as file:
                    self.originalCiphertext = file.read()
                    print(f"Ciphertext Loaded from file: \n{self.originalCiphertext}\n")
            else:
                print("Path to file does not exist")
        else:
            print("We Cannot Load file")

    def options(self, args):
        if (self.module == None):
            print("Please Load a Module first\n")
            return
        #from module.ceasercipher import ceasercipher
        #cc = ceasercipher("aaaa")
        self.module.showOptions()

    def run(self, args):
        self.module.run(args)
        if(self.module.recentSolution != None):
            if(self.module.recentSolutionList == False):
                self.pushResult(self.module.recentSolution, self.modulePath)
            else:
                for r in self.recentSolution:
                    self.pushResult(r, self.modulePath)

    def pathexists(self, arg):
        temppath = self.cwd
        x = None
        if(arg[0] == "/" or arg[0] == "\\"):
            if(arg[0] == "/"):
                arg = "\\" + arg[1:]
            x = temppath+arg
        else:
            x = temppath+"\\"+arg
        #Work Backwards to Get manage .. and . directory
        #remove all . from x
        newPath = ""
        #print(x.split("\\"))
        for subdir in x.split("\\"):
            if(subdir != "."):
                newPath += subdir+"\\"
        newPath = newPath[:-1]
        #Work Backwards to remove all ..
        allowedPaths = []
        fordd = newPath.split("\\")
        i = len(fordd)-1
        while i >= 0:
            if(fordd[i] == ".."):
                i -= 1
            else:
                allowedPaths.append(fordd[i])
            i -= 1
        newPath = ""
        #reverse and concatinate
        for subdir in allowedPaths[::-1]:
            newPath += subdir+"\\"
        newPath = newPath[:-1]
        if(os.path.exists(newPath)):
            return (True, newPath)
        else:
            #check if the arg alone is a valid path to go to
            xAbs = arg
            #Work Backwards to Get manage .. and . directory
            #remove all . from x
            newPath = ""
            #print(x.split("\\"))
            for subdir in xAbs.split("\\"):
                if(subdir != "."):
                    newPath += subdir+"\\"
            newPath = newPath[:-1]
            #Work Backwards to remove all ..
            allowedPaths = []
            fordd = newPath.split("\\")
            i = len(fordd)-1
            while i >= 0:
                if(fordd[i] == ".."):
                    i -= 1
                else:
                    allowedPaths.append(fordd[i])
                i -= 1
            newPath = ""
            #reverse and concatinate
            for subdir in allowedPaths[::-1]:
                newPath += subdir+"\\"
            newPath = newPath[:-1]
            if(os.path.exists(newPath)):
                return (True, newPath)
            else:
                return (False, newPath)


    def pwd(self, args):
        print("Running pwd")
        print(self.cwd)
        pass

    def cd(self, args):
        print("Running cd")
        if(len(args) > 0):
            val, newPath = self.pathexists(args[0])
            if(val):
                self.cwd = newPath
            else:
                print("Change Not Made")
        else:
            print("No Args Specified")

    def ls(self, args):
        print("Running ls")
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
        for d in dirs:
            print("\t\\"+d+"\\")
        for f in files:
            print("\t\\"+f)
