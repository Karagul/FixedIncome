def pvp(rate, pmt, growth=0):
    return pmt / (growth - rate)

def semiannual_spot_rate(discount, maturity):
    return 2 * ( ( 1 / discount ) ** ( 1 / (2 * maturity) ) - 1)

def forward_rate(c_discount, p_discount, periods=1):
    return (p_discount / c_discount - 1) * periods
