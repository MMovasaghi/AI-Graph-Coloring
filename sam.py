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

colorNumber = int(input("Enter Color number : "))

if (colorNumber >= len(inputMatrix)):
    for x in range(len(inputMatrix)):
        print("Node[", x+1, "]: Color[", x+1, "]")
elif (colorNumber <= 0):
    print("ERROR: The Color numebrs must be more than 0")
else:
    obj1 = GraphColoring(inputMatrix, colorNumber)
    obj1.show()