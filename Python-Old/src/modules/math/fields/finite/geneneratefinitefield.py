from parentmodule import module
from types.t_ffieldadditive import t_ffieldadditive

class generatefinitefield(module):
    def __init__(self, ciphertext):
        super().__init__(ciphertext)
        self.runfunction = self.fastpower
        self.setOptions([])

        self.defaultParams = [("Generate Field", ["-q"], [True], [False])]
        #-------------
        self.AddedCommands = []
        self.AddedCommandsFunc = []
        self.AddedCommandsHelp = []
        #Modue Specific varaibles
        #For Quick
        try:
            pass
        except:
            pass
            print(f"One or more of the following " + " " + " were not a valid values respictifully \n\t--setting as default")
