class node:
    def __init__(self, prvNode, number, color):
        self.number = number
        self.prvNode = prvNode
        self.color = color
        self.sons = []