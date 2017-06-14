from bs4 import BeautifulSoup
import urllib3

#Get the HTML code
http = urllib3.PoolManager()
response = http.request('GET' , 'www.puzzle-bridges.com/?size=0')
page_source = response.data

#Make it readable
soup = BeautifulSoup(page_source , 'html.parser')

#Display it (for now)
print(soup.prettify())
