class GraphColoring:
    def __init__(self, adjMatrix, colorNumber):
        self.adjMatrix = adjMatrix
        self.colorNumber = colorNumber
        self.colorMatrix = []

    def show(self):
        print("Graph Adjacent Matrix: ")
        print(self.adjMatrix)
        print("Color number : ", self.colorNumber)
    
    def coloring(self):
        print("Coloring")

    def forwardChecking(self):
        print("ForwardCheking")

    def arcConsistancyChecking(self):
        print("arcConsistancyChecking")

    def showResult(self, status):
        if (status == 1):
            print(">> Result:")
            for x in range(self.colorNumber):
                print(">>>> Node[",x+1,"] : Color[",self.colorMatrix[x],"]")
        else:
            print("There is no way to coloring the graph with these number of colors.")