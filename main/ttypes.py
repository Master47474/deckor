

class types():

    def __init__(self):
        self.Types = {"undefined": -1, "none": 0, "unicode": 1}

    def determineType(self, typeStr):
        return self.Types[typeStr]
