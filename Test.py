from unittest import TestCase
from bs4 import BeautifulSoup
import Exoplanet

class TransitTestCase(TestCase):
     def test_per(self):
            html_str = """
            <!DOCTYPE html>
            <html>
            <head> 
            <title> Pars </title>
            <meta charset = "utf - 8">
            </head>
            <body>
            <td id="planet_period_0" rowspan="1">1.5 (&#177; 3.8e-07) day</td>
            </body>
            </html>
            """
            with open("Pars.html",'w',encoding = 'utf-8') as f:
                   f.write(html_str)
                   f.close()

            with open("Pars.html", "r") as f:
    
                   contents = f.read()
 
                   soup = BeautifulSoup(contents, 'lxml')
            
            self.assertEqual(Exoplanet.per(soup), 1.5)            
		
     def test_transit(self):
            for n in range(0, 20):
                   self.assertEqual(Exoplanet.Transit(1, 0, 0, 20)[n], n)