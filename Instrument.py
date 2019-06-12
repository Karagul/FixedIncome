class Instrument():

    """ a smiple fixed income model """

    def __init__(self, maturities=[], discounts=[], cash_flows=[]):
        """ initialize data """
        self.maturities = [float(x) for x in maturities]
        self.discounts = [float(x) for x in discounts]
        self.cash_flows = [float(x) for x in cash_flows]
