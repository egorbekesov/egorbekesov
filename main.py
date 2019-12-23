import numpy as np
from bs4 import BeautifulSoup
import requests as req
import Exoplanet

name = input("Enter name of planet.")

first_date = float(input("Enter the first day of observations"))

end_date = float(input("Enter the last day of observations"))

period = Exoplanet.per(name)

last_transit = Exoplanet.ltr(name)


Exoplanet.Transit(period, last_transit, first_date, end_date)



