"""
Finite Fields Formed Under Addition
Id element = 0
Inverse Element = x*x^-1 = 0
Ord(element) = el + el + el + ... + el = id (n times) = n
"""

class GroupElement():
    def __init__(self, value):
        self.value = value
        pass

class FiniteGroupElement(GroupElement):
    def __init__(self, value, modulo):
        super().__init__(value)
        self.modulo = modulo


class t_ffieldadditive():
    def __init__(self, n, generator):
        if(generator > n):
            raise indexerror
        self.id = 0
        self.modulo = n
        self.generator = generator
        self.elementsOrder = [] #of form (element, order), as it will be calcualted simultaniously

        #index being for additive fields
        currElement = generator
        i = 0
        # Do Not Deal with infintie loops yet
        # ONLY USE ELEMENTS THAT ARE GENERATORS
        while ( (currElement + generator) % self.modulo != generator):
            self.elementsOrder.append((currElement, self.deduceOrder(currElement)))
            currElement += generator
            currElement = currElement% self.modulo
            i += 1
        self.elementsOrder.append((currElement, 1))


    def deduceOrder(self, element):
        ord = 1
        temp = element
        while((temp + element) % self.modulo != element):
            ord += 1
            temp += element
        return ord

    def orders(self):
        return [o for _,o in self.elementsOrder]

    def __str__(self):
            return ",".join([str(el) for el,_ in self.elementsOrder])


    #Setters and Getters
    def getId(self):
        return self.id

    def getModulo(self):
        return self.modulo

    def getElementsOrder(self):
        return self.elementsOrder

    def getElements(self):
        return [o for _,o in self.elementsOrder]




""" testing """
f1 = t_ffieldadditive(7, 1)
print("Done 1")
f2 = t_ffieldadditive(7, 1)
print("Done 2")
f3 = t_ffieldadditive(7, 3)
print("Done 3")
f4 = t_ffieldadditive(7, 4)
print("Done 4")
f5 = t_ffieldadditive(7, 5)
print("Done 5")
f6 = t_ffieldadditive(7, 6)
print("Done 6")
f7 = t_ffieldadditive(16, 2)

f = [f1, f2, f3, f4, f5, f6, f7]
for ff in f:
    print(ff)
    print(ff.orders())
