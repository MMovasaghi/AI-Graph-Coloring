from GraphClass import GraphColoring
    
#input paramiters--------------------------
#the Graph Adjacent Matrix has default value:
inputMatrix =   [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]
                ]
colorNumber = 5
#------------------------------------------
# get number of color
colorNumber = int(input("Enter Color number : "))
# read matrix as text in 
with open("inputMatrix.txt") as textFile:
    lines = [line.split() for line in textFile]
print("==============================================\n>> Inputs:")
print(">>>> Input Adjacency Matrix:")
print(lines)
print("----------------------------------------------")
print(">>>> Number of Colors that can use:", colorNumber)
matrixLen = len(lines)
# check if number of color more than the number of node it isn't need the calculation
if (colorNumber >= matrixLen):
    print("==============================================\n>> Result:")
    for x in range(matrixLen):
        print(">>>> Node[", x+1, "]: Color[", x+1, "]")
elif (colorNumber <= 0):
    print("==============================================\n>> Result:")
    print("ERROR: The Color numebrs must be more than 0")
else: # The main calculation
    obj1 = GraphColoring(lines, colorNumber)
    #obj1.show()
    obj1.coloring()
