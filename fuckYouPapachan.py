from bs4 import BeautifulSoup
import os
import urllib3

#Get the HTML code
http = urllib3.PoolManager()
response = http.request('GET' , 'www.puzzle-bridges.com/?size=11')

#size 11 is a 25x25 hard puzzle, which is what we should be importing, but I have size=0
#uncommented for now since it's a smaller file to read as that board is only 7x7
#response = http.request('GET' , 'www.puzzle-bridges.com/?size=11')

page_source = response.data

#Make it readable
soup = BeautifulSoup(page_source , 'html.parser')
for line in soup.get_text().split("\n") :
    if line.startswith("25x25") :
        ID = line[-9:].replace(',' , '')
        print("ID : {}".format(ID))
        response2 = http.request('GET' , "www.puzzle-bridges.com/task.php?id=" + ID + "&size=11")
    elif line.startswith("wall[") :
        print(line)

page_source2 = response2.data
soup2 = BeautifulSoup(page_source2 , 'html.parser')
try :
    os.remove("Image.png")
except OSError:
    pass

f = open("Image.png" , "w")
f.write(soup2.get_text())
