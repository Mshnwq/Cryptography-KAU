
class Battalion:

    def __init__(self, algorithim, key):
        self.algorithm = algorithim
        self.key = key

    def getAlgorithm(self):
        return self.algorithm
    def setAlgorithm(self, newAlgorithm):
        self.algorithm = newAlgorithm
    def getKey(self):
        return self.key
    def setKey(self, newKey):
        self.key = newKey