from fourMarking import *

class relation:
    def __init__(self, lefthandside, righthandside):
        # Set LHS of relation to given LHS
        self.lefthandside = lefthandside
        # Set RHS of relation to given RHS
        self.righthandside = righthandside

    

vertex = new relation(new fourMarking([CrossingType.VERTEX]), [new fourMarking([CrossingType.VERTEX])])