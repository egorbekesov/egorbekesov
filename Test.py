from unittest import TestCase
import Exoplanet

class TransitTestCase(TestCase):
     def test_transit(self):
            for n in range(0, 20):
                   self.assertEqual(Exoplanet.Transit(1, 0, 0, 20)[n], n)