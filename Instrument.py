class Instrument():

    """ a simple fixed income model """

    def __init__(self, discounts=[], cash_flows=[], ppy=1):
        """ initialize data """
        self.discounts = [float(x) for x in discounts]
        self.cash_flows = [float(x) for x in cash_flows]
        self.ppy = ppy

    def price(self):
        p = 0
        i = 0
        while (i < len(self.discounts)):
            p += self.discounts[i] * self.cash_flows[i]
            i += 1
        return p

    def macauley_duration(self):
        md = 0
        i = 0
        while (i < len(self.maturities)):
            pvcf = self.discounts[i] * self.cash_flows[i]
            md += (i+1) * pvcf
            i += 1
        return md / self.ppy

    def modified_duration(self):
        return self.macaulay_duration() * self.discounts[0]

    def convexity(self):
        c = 0
        i = 0
        while (i < len(self.discounts)):
            pvcf = self.discounts[i] * self.cash_flows[i]
            c += (i+1) * (i+2) * pvcf
            i += 1
        c = (c * (self.discounts[0]**2)) / self.price()
        return c / (self.ppy ** 2)

