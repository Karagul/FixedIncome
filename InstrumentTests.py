import unittest
import FixedIncome
from Instrument import Instrument

class Duration(unittest.TestCase):
    def test_modified_duration(self):
        r = 0.0500
        d = []
        cf = []
        i = 0
        while (i < 10):
            d.append(FixedIncome.discount(spot=r, nper=i+1))
            cf.append(7)
            i += 1
        cf[len(cf)-1] += 100
        my_instrument = Instrument(discounts=d, cash_flows=cf, ppy=2)
        self.assertEqual(round(my_instrument.modified_duration(),2), 3.67)
        

class Convexity(unittest.TestCase):
    def test_convexity(self):
        r = 0.0500
        d = []
        cf = []
        i = 0
        while (i < 10):
            d.append(FixedIncome.discount(spot=r, nper=i+1))
            cf.append(4)
            i += 1
        cf[len(cf)-1] += 100
        my_instrument = Instrument(discounts=d, cash_flows=cf, ppy=2)
        self.assertEqual(round(my_instrument.convexity(),2), 19.57)

unittest.main()
