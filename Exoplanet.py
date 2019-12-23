import numpy as np
from bs4 import BeautifulSoup
import requests as req

def pars(name):
    
    """
    name - name of exoplanet. Example: tres-3_b
    
    """

    resp = req.get("http://exoplanet.eu/catalog/" + name + "/")
 
    soup = BeautifulSoup(resp.text, 'lxml')

    return soup

def per(soup):
    
    """
    soup - file creating after parsing calalog page
    
    period - orbital period of exoplanet
    
    """

    period = soup.find(id="planet_period_0").text

    period = float(period.split(" ")[0])
    
    return period

def ltr(soup):
    
    """
    last_transit - julian date of the last observed transit mentined in catalog
    
    """

    last_transit = soup.find(id="planet_tzero_tr_0").text

    last_transit = float(last_transit.split(" ")[0])
    
    return last_transit


def Transit(period, last_transit, first_date, end_date): 
    
    """ 
    first_date and end_date - julian dates of days when observations start and finished
    
    n0 and n1 - number of planet rotations between last transit in catalog and dates jf start and finish of observations
    
    transit_date - array with jullian dates of all transits in chosen time
    
    """
    
    n0 = int((first_date - last_transit)//period)

    n1 = int((end_date - last_transit)//period)
    
    transit_date = np.zeros(n1 - n0)
    
    for n in range(n0, n1):
        transit_date[n - n0] = last_transit + n*period
    
    return transit_date

