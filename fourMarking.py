from enum import Enum

class crossingType(Enum):
    NONE = 0
    VERTEX = 1
    POSITIVE = 2
    NEGATIVE = 3

class fourMarking:
    
    def __init__(self, stacking_list):
        self.stacking_list = stacking_list

    def printStacking(self):
        print(self.stacking_list)
