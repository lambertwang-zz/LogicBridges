import os

try :
    os.remove("nodes.txt")
except OSError :
    pass

f = open("output.txt" , "r")
f2 = open("nodes.txt" , "w")

lines = f.readlines()
for l in lines :
    for c in l :
        if c != '\n' and c != ' ' :
            f2.write(c)
f2.write('\n')
