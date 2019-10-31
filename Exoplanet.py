import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://exoplanet.eu/catalog/tres-3_b/" 

page = urlopen(url)

soup=BeautifulSoup(page.read())

value = soup.findAll(attrs={"class":"rowspan"})

print(value[1])
