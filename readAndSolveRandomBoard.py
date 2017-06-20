from bs4 import BeautifulSoup
# import pyperclip
import time
import re
import os
import sys
import urllib3

# Local file
from solver import *

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.puzzle-bridges.com/?size=11')

xPos = []
yPos = []
toWrite = open("pageData.html" , "w")
toWrite.write(r.data)
toWrite.close()

readFile = open("pageData.html" , "r")
fileLines = readFile.readlines()
walls = 0


for line in fileLines :
    if line.find("25x25") != -1 :
        ID = line[-14:-5].replace(',' , '')
        print("ID : {}".format(ID))
    elif line.find("wall[") != -1 :
        matches = re.findall(r"\[(\w+)\]" , line)
        if len(matches) == 2 :
            try :
                xPos.append(eval(matches[1]))
                yPos.append(eval(matches[0]))
                walls = walls + 1
                print(line + " : {}".format(walls))
            except :
                pass


try :
    os.remove("Image.png")
    os.remove("board.data")
except OSError :
    pass

print("found : {} walls".format(walls))

os.system("curl \"www.puzzle-bridges.com/task.php?id=" + ID + "\&size=11\" > Image.png")
os.system("tesseract -psm 6 --tessdata-dir . Image.png output -l mylang")
os.system("python3 removeExcess.py")
time.sleep(0.1)

nodesFile = open("nodes.txt" , "r")
nodeLines = nodesFile.readlines()
nodes = []
for l in nodeLines :
    for c in l :
        if c != '\n' :
            nodes.append(c)

f = open("board.data" , "w")



count = 0
for y in range(25) :
    for x in range(25) :
        if count == walls - 1 :
            break
        if xPos[count] == x and yPos[count] == y :
            f.write(nodes[count])
            count = count + 1
        else :
            f.write('x')
    f.write('\n')
f.close()

startTime = time.time()
filePath = "board.data"
nodes = readIntoData(filePath)
for n in nodes :
    print("Neighbors of node {} : ".format(n.n))
    print(getNeighbors(n , nodes))
    print("Number : {}".format(numNeighbors(n , nodes)))

solveBoard(nodes)

for b in bridges :
    print("Bridge : {} to {}".format(b.n1 , b.n2))

print()
solution = printBoard(filePath , nodes)

endTime = time.time()

print("Total time : {}".format(endTime - startTime))

print(solution)
# pyperclip.copy(solution)
