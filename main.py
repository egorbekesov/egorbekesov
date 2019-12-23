import numpy as np
from bs4 import BeautifulSoup
import requests as req
import Exoplanet

name = input("Enter name of planet.")

soup = Exoplanet.pars(name)

first_date = float(input("Enter the first day of observations"))

end_date = float(input("Enter the last day of observations"))

period = Exoplanet.per(soup)

last_transit = Exoplanet.ltr(soup)

transit_date = Exoplanet.Transit(period, last_transit, first_date, end_date)

for i in range(0, len(transit_date)):
      print(transit_date[i])
