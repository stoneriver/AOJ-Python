class Dice():
    def __init__(self, numbers):
        self.numbers = numbers
        self.topIndex = 1
        self.frontIndex = 2
        self.rightIndex = 3
        self.leftIndex = 4
        self.backIndex = 5
        self.bottomIndex = 6
    
    def getNumberOnSide(sideIndex):
        return self.numbers[sideNum - 1]
    
    def getTopIndex():
        return topIndex
    
    def getTopNumber():
        return getNumberOnSide(topIndex)
    
    def getFrontIndex():
        return frontIndex
    
    def getFrontNumber():
        return getNumberOnSide(frontIndex)
    
    def getRightIndex():
        return rightIndex
    
    def getRightNumber():
        return getNumberOnSide(rightIndex)
    
    