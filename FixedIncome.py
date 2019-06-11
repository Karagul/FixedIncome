def discount(spot, nper=1):
    """ returns discount factor """
    return 1 / ( (1 + spot) ** nper)

def pv(rate, nper, pmt=0.0, fv=0.0):
    """ returns present value """
    d = discount(rate)
    pv = 0
    i = 1
    while (i <= nper):
        pv += pmt * (d**i)
        i += 1
    pv += fv * (d**nper)
    return pv

def fv(rate, nper, pv=0.0, pmt=0.0):
    """ returns future value """
    d = discount(rate)
    fv = 0
    i = 1
    while (i <= nper):
        fv += pmt / (d ** (nper-i))
        i += 1
    fv += pv / (d ** nper)
    return fv

def rate(nper, pmt, present_value, future_value):
    """ returns rate """
    """ while this technically works as-is, should implement using n-r l8r """
    """ hella slow, just use np.rate for now """
    guess = .010000
    while True:
        rate_pv = -pv(rate=guess, nper=nper, pmt=pmt, fv=future_value)
        print(rate_pv)
        if(round(rate_pv,4) == round(present_value,4)):
            return guess
        if (rate_pv < present_value):
            guess += .000000001
        else:
            guess -= .000000001
    
    
def pvp(rate, pmt, growth=0):
    """ returns present value factor of a perpetuity """
    return pmt / (growth - rate)

def semiannual_spot_rate(discount, maturity):
    return 2 * ( ( 1 / discount ) ** ( 1 / (2 * maturity) ) - 1)

def forward_rate(c_discount, p_discount, periods=1):
    """ returns the forward rate from the current and previous discount factors """
    """ periods is the annualization factor """
    return (p_discount / c_discount - 1) * periods
