bridges = []


class Node:
    def __init__(self, xpos, ypos, val, name):
        self.x = xpos
        self.y = ypos
        self.v = val
        self.n = name

class Bridge:
    def __init__(self, node1Name , node2Name):
        self.n1 = node1Name
        self.n2 = node2Name

#Creates a bridge between 2 nodes.
#It is assumed that this bridge can be created.
def formBridge(node1 , node2) :
    global bridges
    node1.val = node1.val - 1
    node2.val = node2.val - 1
    bridges.apppend(Bridge(node1.v , node2.v))

#Reads the board from the given file and
#returns the proper node array
def readIntoData(filePath) :
    names = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    f = open(filePath , "r")
    lines = f.readlines()
    y = 1
    x = 1
    nodes = []
    count = 0
    for l in lines :
        x = 1
        for c in l :
            if c == 'x' or c == '\n' :
                pass;
            else :
                val = eval(c)
                nodes.append(Node(x , y , val , names[count]))
                count = count + 1
            x = x + 1
        y = y + 1
    return nodes


def solveTrivialNode(node , nodes , bridges) :
    #TODO
    print("to be implemented")

#Returns a list of all the neighboring nodes
def getNeighbors(node , nodes) :
    closest = 99
    #Format : [Down , Up , Left , Right]
    neighbors = ['' , '' , '' , '']
    counter = 0
    found = ''
    for n in nodes :
        if node.x == n.x and (node.y - n.y != 0) and (abs(node.y - n.y) < closest) and (n.y > node.y):
            closest = abs(node.y - n.y)
            found = n.n
    if closest != 99 :
        neighbors[counter] = found
    counter = counter + 1

    closest = 99
    found = ''
    for n in nodes :
        if node.x == n.x and (node.y - n.y != 0) and (abs(node.y - n.y) < closest) and (n.y < node.y):
            closest = abs(node.y - n.y)
            found = n.n
    if closest != 99 :
        neighbors[counter] = found
    counter = counter + 1

    closest = 99
    found = ''
    for n in nodes :
        if node.y == n.y and (node.x - n.x != 0) and (abs(node.x - n.x) < closest) and (n.x < node.x):
            closest = abs(node.x - n.x)
            found = n.n
    if closest != 99 :
        neighbors[counter] = found
    counter = counter + 1

    closest = 99
    found = ''
    for n in nodes :
        if node.y == n.y and (node.x - n.x != 0) and (abs(node.x - n.x) < closest) and (n.x > node.x):
            closest = abs(node.x - n.x)
            found = n.n
    if closest != 99 :
        neighbors[counter] = found
    counter = counter + 1

    return neighbors

nodes = readIntoData('sample7x7Board.data')

for n in nodes :
    print("Neighbors of node {} : ".format(n.n))
    print(getNeighbors(n , nodes))

