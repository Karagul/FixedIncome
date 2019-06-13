class Instrument():

    """ a simple fixed income model """

    def __init__(self, discounts=[], cash_flows=[], ppy=1):
        """ initialize data """
        self.discounts = [float(x) for x in discounts]
        self.cash_flows = [float(x) for x in cash_flows]
        self.ppy = ppy

    def macaulay_duration(self):
        md = 0
        pvcf = 0
        i = 0
        while (i < len(self.discounts)):
            i_pvcf = self.discounts[i] * self.cash_flows[i]
            pvcf += i_pvcf
            md += (i+1) * i_pvcf
            i += 1
        return md / (self.ppy * pvcf)

    def modified_duration(self):
        return self.macaulay_duration() * self.discounts[0]

    def convexity(self):
        c = 0
        pvcf = 0
        i = 0
        while (i < len(self.discounts)):
            i_pvcf = self.discounts[i] * self.cash_flows[i]
            pvcf += i_pvcf
            c += (i+1) * (i+2) * i_pvcf
            i += 1
        return (c * (self.discounts[0]**2)) / (pvcf * (self.ppy ** 2))

