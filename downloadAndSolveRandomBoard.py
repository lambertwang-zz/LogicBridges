from bs4 import BeautifulSoup
import re
import os
import urllib3

xPos = []
yPos = []

#Get the HTML code
http = urllib3.PoolManager()
response = http.request('GET' , 'www.puzzle-bridges.com/?size=11')

page_source = response.data

#Make it readable
soup = BeautifulSoup(page_source , 'html.parser')
for line in soup.get_text().split("\n") :
    if line.startswith("25x25") :
        ID = line[-9:].replace(',' , '')
        print("ID : {}".format(ID))
    elif line.find("wall[") != -1 :
        print(line)
        matches = re.findall(r"\[(\w+)\]" , line)
        if len(matches) == 2 :
            print(matches[0])
            print(matches[1])
            try :
                xPos.append(eval(matches[1]))
                yPos.append(eval(matches[0]))
            except :
                pass


try :
    os.remove("Image.png")
    os.remove("board.data")
except OSError :
    pass

os.system("curl \"www.puzzle-bridges.com/task.php?id=" + ID + "\&size=11\" > Image.png")
os.system("./readImage.sh")
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
        if xPos[count] == x and yPos[count] == y :
            f.write(nodes[count])
            count = count + 1
        else :
            f.write('x')
    f.write('\n')
f.close()

os.system("python3 solveBoard.py board.data")
