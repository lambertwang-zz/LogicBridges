
class Node:
    def __init__(self, xpos, ypos, val, name):
        self.x = xpos
        self.y = ypos
        self.v = val
        self.n = name

def getNeighbors(node , nodes) :
    closest = 99
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

nodes = [Node(1,1,2,'A') , Node(5,1,4,'B') , Node(7,1,1,'C') , Node(7,4,2,'D') , Node(1,6,2,'E') , Node(3,6,1,'F') , Node(2,7,2,'G') , Node(5,7,4,'H') , Node(7,7,3,'I')]

for n in nodes :
    print("Neighbors of {} : ".format(n.n))
    print(getNeighbors(n , nodes))

