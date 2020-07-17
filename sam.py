# from GraphClass import GraphColoring
# from node import node     
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
# colorNumber = int(input("Enter Color number : "))
# # read matrix as text in 
# with open("inputMatrix.txt") as textFile:
#     lines = [line.split() for line in textFile]
# print(lines)
# matrixLen = len(lines)
# # check if number of color more than the number of node it isn't need the calculation
# if (colorNumber >= matrixLen):
#     for x in range(matrixLen):
#         print("Node[", x+1, "]: Color[", x+1, "]")
# elif (colorNumber <= 0):
#     print("ERROR: The Color numebrs must be more than 0")
# else: # The main calculation
#     obj1 = GraphColoring(lines, colorNumber)
#     obj1.show()

# root = node(None,1,5)
# node1 = node(root,2,6)
# node2 = node(root,2,1)
# root.sons.append(node1)
# root.sons.append(node2)
# node2.sons.append(node1)
# print(root.sons[1].sons[0].color)



colors = [i for  i in range(1)]
colors.remove(0)
if len(colors) >= 1:
    print("yes")
print(colors)