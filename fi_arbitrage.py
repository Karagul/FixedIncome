import csv
from datetime import datetime

def matching_strip(date):
    i = 0
    while (i < len(strips)):
        if (strips[i][0] == date):
            return strips[i]
        i += 1
    return False

# extract
with open("strips.csv") as f:
    strips = []
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        strips.append(row)
with open("treasuries.csv") as f:
    treasuries = []
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        treasuries.append(row)

# transform
i = 0
while (i < len(strips)):
    strips[i][0] = datetime.strptime(strips[i][0], '%m/%d/%y')
    strips[i][1] = float(strips[i][1])
    i += 1
i = 0
while (i < len(treasuries)):
    treasuries[i][0] = datetime.strptime(treasuries[i][0], '%m/%d/%y')
    treasuries[i][1] = float(treasuries[i][1])
    treasuries[i][2] = float(treasuries[i][2])
    i += 1

# arbitrage
i = 0
while (i < len(treasuries)):
    my_treasury = treasuries[i]
    j = i+1
    while (j < len(treasuries)):
        if (my_treasury[0] == treasuries[j][0]):
            my_strip = matching_strip(my_treasury[0])
            if (my_strip):
                coupon_ratio = treasuries[j][2] / my_treasury[2]
                shares = coupon_ratio
                strip_shares = coupon_ratio - 1
                t1_price = shares * my_treasury[1]
                t2_price = treasuries[j][1]
                s_price = strip_shares * my_strip[1] 
                print("")
                print("Arbitrage found!")
                if (t1_price < t2_price + s_price):
                    print("Sell:")
                    print("1 share of: " + str(treasuries[j]) + " for " + 
                            str(round(t2_price,2)))
                    print(str(round(strip_shares,2)) + " shares of: " + str(my_strip) + 
                            " for " + str(round(s_price,2)))
                    print("Buy:")
                    print(str(round(shares,2)) + " shares of: " + str(my_treasury) + " for " + 
                            str(round(t1_price,2)))
                else:
                    print("Sell:")
                    print(str(round(shares,2)) + " shares of: " + str(my_treasury) + " for " + 
                            str(round(t1_price,2)))
                    print("Buy:")
                    print("1 share of: " + str(treasuries[j]) + " for " + 
                            str(round(t2_price,2)))
                    print(str(round(strip_shares,2)) + " shares of: " + str(my_strip) + 
                            " for " + str(round(s_price,2)))
        j += 1
    i += 1
            
