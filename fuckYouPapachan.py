from bs4 import BeautifulSoup
import urllib3

#Get the HTML code
http = urllib3.PoolManager()
response = http.request('GET' , 'www.puzzle-bridges.com/?size=0')

#size 11 is a 25x25 hard puzzle, which is what we should be importing, but I have size=0
#uncommented for now since it's a smaller file to read as that board is only 7x7
#response = http.request('GET' , 'www.puzzle-bridges.com/?size=11')

page_source = response.data

#Make it readable
soup = BeautifulSoup(page_source , 'html.parser')

#Display it (for now)
print(soup.prettify())
