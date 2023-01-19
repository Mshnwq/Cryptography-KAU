from battalion import Battalion
class Solider:
    
    def __init__(self, name, battalion):
        self.name = name
        self.battalion = battalion
    
    def getName(self):
        return self.name
    
    def getBattalion(self):
        return self.battalion
    
    def setName(self, name):
        self.name = name
    def setBattalion(self, battalion):
        self.battalion = battalion