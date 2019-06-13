import unittest
import FixedIncome
from Instrument import Instrument

class Convexity(unittest.TestCase):
    # Create test data
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
