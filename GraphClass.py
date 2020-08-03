from node import node
class GraphColoring:
    def __init__(self, adjMatrix, colorNumber):
        self.adjMatrix = adjMatrix
        self.colorNumber = colorNumber
        self.nodeNumber = len(adjMatrix)
        self.colorMatrix = [-1]*self.nodeNumber
        self.colors = [i for i in range(colorNumber)]

    def show(self):
        print("Graph Adjacent Matrix: ")
        print(self.adjMatrix)
        print("Color number : ", self.colorNumber)
    
    def coloring(self):
        root = node(None,0,0)
        currentNumber = 0
        result = self.coloringSubFunction(currentNumber, root)
        self.showResult(result)

    def coloringSubFunction(self, currentNumber, current):
        
        for i in range(self.nodeNumber):            
            if(self.colorMatrix[i] == -1):
                currentNumber = i
                nextNode = self.canOpen(currentNumber)
                #print("$ i[", currentNumber ,"]: nextNode[", nextNode ,"]")
                while (nextNode > 0): # the number of next node that must be open, IF it is -1, it means that there is no node to open it

                    colors =  [i for i in range(self.colorNumber)]
                    self.forwardChecking(colors, currentNumber)

                    if ((len(colors) > 0) and (nextNode != -1)):                        
                        
                        self.colorMatrix[currentNumber] = colors[0]

                        newNode = node(current, nextNode, -1)
                        current.sons.append(newNode)                        

                        current = current.sons[0]

                        currentNumber = nextNode

                        nextNode = self.canOpen(currentNumber)
                    else:
                        return False
                if(nextNode == -1):
                    colors =  [i for i in range(self.colorNumber)]
                    self.forwardChecking(colors, currentNumber)
                    self.colorMatrix[currentNumber] = colors[0]
        return True

    def forwardChecking(self, colors, number):
        for k in range(self.nodeNumber):
            if (self.adjMatrix[number][k] == '1' and self.colorMatrix[k] != -1):
                if self.colorMatrix[k] in colors: colors.remove(self.colorMatrix[k]) #remove connection colors

        #print("> Node[",number,"]: posible color:",colors)

    def canOpen(self, number):
        for i in range(self.nodeNumber):
            if (self.adjMatrix[number][i] == '1' and self.colorMatrix[i] == -1):
                return i
        return -1

    
    def showResult(self, status):
        if (status):
            print("==============================================\n>> Result:")
            for x in range(len(self.colorMatrix)):
                print(">>>> Node[",x,"] : Color[",self.colorMatrix[x],"]")
        else:
            print("There is no way to coloring the graph with these number of colors.")