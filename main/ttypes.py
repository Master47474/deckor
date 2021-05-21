

class types():

    def __init__(self):
        self.Types = {"undefined": -1, "none": 0, "unicode": 1}

    def determineType(self, typeStr):
        return self.Types[typeStr]

    def getType(self, type):
        for t in self.Types:
            if(self.Types[t] == type):
                return t
