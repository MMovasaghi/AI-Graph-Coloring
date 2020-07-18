from node import node
class GraphColoring:
    def __init__(self, adjMatrix, colorNumber):
        self.adjMatrix = adjMatrix
        self.colorNumber = colorNumber
        self.nodeNumber = len(adjMatrix)
        self.colorMatrix = [-1]*self.nodeNumber
        self.colors = [i for  i in range(colorNumber)]

    def show(self):
        print("Graph Adjacent Matrix: ")
        print(self.adjMatrix)
        print("Color number : ", self.colorNumber)
    
    def coloring(self):
        root = node(None,0,0)
        self.colorMatrix[0] = 0
        currentNumber = 0
        self.coloringSubFunction(currentNumber, root)
        self.showResult(1)     

    def coloringSubFunction(self, currentNumber, current):
        colors = self.colors
        self.forwardChecking(colors, currentNumber)
        if len(colors) > 0:
            check = False
            for j in range(self.nodeNumber):
                if self.adjMatrix[currentNumber][j] == '1' and self.colorMatrix[j] == -1 and not check:
                    check = True
                    print(">> Node[",current.number+1,"] : color:",colors,"")
                    print(">> Node[",current.number+1,"] : color[",current.color,"]") 
                    for x in range(len(colors)):
                        newNode = node(current, j, colors[x])
                        current.sons.append(newNode)
                    
                    current = current.sons[0]
                    self.colorMatrix[j] = current.color
                    currentNumber = current.number
                    self.forwardChecking(colors, current.number)
                    break
            
            if not check:
                self.colorMatrix[currentNumber] = 0
            self.coloringSubFunction(currentNumber, current)
        else: # there is no color
            return False        

    def forwardChecking(self, colors, nodeNumber):
        for k in range(self.nodeNumber):
            if (self.adjMatrix[nodeNumber][k] == '1'):
                if self.colorMatrix[k] in colors: colors.remove(self.colorMatrix[k]) #remove connection colors

        print("> Node[",nodeNumber+1,"]: color:",colors)

    def arcConsistancyChecking(self):
        print("arcConsistancyChecking")

    
    def showResult(self, status):
        if (status == 1):
            print(">> Result:")
            for x in range(len(self.colorMatrix)):
                print(">>>> Node[",x+1,"] : Color[",self.colorMatrix[x],"]")
        else:
            print("There is no way to coloring the graph with these number of colors.")