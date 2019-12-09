import numpy as np
from bs4 import BeautifulSoup
import requests as req

name = input("Enter name of planet.")

first_date = float(input("Enter start date of observations."))

end_date = float(input("Enter final date of observations."))

resp = req.get("http://exoplanet.eu/catalog/" + name + "/")
 
soup = BeautifulSoup(resp.text, 'lxml')

period = soup.find(id="planet_period_0").text

period = float(period.split(" ")[0])

last_transit = soup.find(id="planet_tzero_tr_0").text

last_transit = float(last_transit.split(" ")[0])

n0 = int((first_date - last_transit)/period)

n1 = int((end_date - last_transit)/period)

for n in range(n0+1, n1):
    transit_date = last_transit + n*period
    print(transit_date)
