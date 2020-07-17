from node import node
class GraphColoring:
    def __init__(self, adjMatrix, colorNumber):
        self.adjMatrix = adjMatrix
        self.colorNumber = colorNumber
        self.nodeNumber = len(adjMatrix)
        self.colorMatrix = [-1]*nodeNumber
        self.colors = [i for  i in range(colorNumber)]

    def show(self):
        print("Graph Adjacent Matrix: ")
        print(self.adjMatrix)
        print("Color number : ", self.colorNumber)
    
    def coloring(self):
        root = node(None,0,0)
        self.colorMatrix[0] = 0
        current = root
        for i in range(self.nodeNumber)
            colors = self.colors
            self.forwardChecking(colors, i)
            if len(colors) > 0:
                check = False
                for j in range(self.nodeNumber)
                    if self.adjMatrix[i][j] == '1' and self.colorMatrix[j] == -1:
                        check = True
                        for x in range(len(colors))
                            newNode = node(current, j, colors[x])
                            current.sons.append(newNode)
                        
                        current = current.sons[0]
                        self.colorMatrix[j] = current.color
                        break

                if not check:
                    self.colorMatrix[i] = 0
                if check:   
                    i = current.number
                    
            else: # there is no color
                if current != root:
                    self.colorMatrix[current.number] = -1
                    current = current.prvNode
                    

    def forwardChecking(self, colors, nodeNumber):
         for k in range(self.nodeNumber)
            if self.adjMatrix[i][k] == '1':
                colors.remove(self.colorMatrix[j]) #remove connection colors

    def arcConsistancyChecking(self):
        print("arcConsistancyChecking")

    
    def showResult(self, status):
        if (status == 1):
            print(">> Result:")
            for x in range(self.colorNumber):
                print(">>>> Node[",x+1,"] : Color[",self.colorMatrix[x],"]")
        else:
            print("There is no way to coloring the graph with these number of colors.")