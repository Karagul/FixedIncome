import csv, math, numpy
import FixedIncome
from sklearn.linear_model import LinearRegression

# extract
with open("strips_curve.csv") as f:
    s_data = []
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        s_data.append(row)
with open("treasury_curve.csv") as f:
    t_data = []
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        t_data.append(row)

# transform
i = 0
s_maturity = []
s_maturity_2 = []
s_maturity_3 = []
s_maturity_4 = []
s_maturity_5 = []
s_px = []
s_discount = []
s_ln_discount = []
s_spot = []
s_forward = []
while (i < len(s_data)):
    s_maturity.append(float(s_data[i][0]))
    s_maturity_2.append(s_maturity[i]**2)
    s_maturity_3.append(s_maturity[i]**3)
    s_maturity_4.append(s_maturity[i]**4)
    s_maturity_5.append(s_maturity[i]**5)
    s_px.append(float(s_data[i][1]))
    s_discount.append(s_px[i]/100)
    s_ln_discount.append(math.log(s_discount[i]))
    s_spot.append(FixedIncome.semiannual_spot_rate(s_discount[i], s_maturity[i]))
    if (i > 0):
        s_forward.append(FixedIncome.forward_rate(s_discount[i], s_discount[i-1], periods=4))
    else:
        s_forward.append("N/M")
    i += 1

i = 0
t_px = []
t_maturity = []
t_coupon = []
t_yield = []
while (i < len(t_data)):
    t_px.append(float(t_data[i][0]))
    t_maturity.append(float(t_data[i][1]))
    t_coupon.append(float(t_data[i][2]))
    t_yield.append(float(t_data[i][3]))
    i += 1
'''
print("---- QUESTION 1 ----")
print("maturity,price,discount,spot,forward")
i = 0
while (i < len(s_data)):
    if (i > 0):
        print(str(round(s_maturity[i],2)), str(round(s_px[i],2)), str(round(s_discount[i],4)),
                str(round(s_spot[i],4)), str(round(s_forward[i],4)))
    else:
        print(str(round(s_maturity[i],2)), str(round(s_px[i],2)), str(round(s_discount[i],4)),
                str(round(s_spot[i],4)))
    i += 1
'''
print("---- QUESTION 2 ----")

# Step 1: Build numpy arrays
x = []
i = 0
while (i < len(s_data)):
    row = []
    row.append(s_maturity[i])
    row.append(s_maturity_2[i])
    row.append(s_maturity_3[i])
    row.append(s_maturity_4[i])
    row.append(s_maturity_5[i])
    x.append(row)
    i += 1
y = s_ln_discount
x, y = numpy.array(x), numpy.array(y)

# Step 2: Create model
model = LinearRegression().fit(x, y)

# Step 3: Retrieve score
r_sq = model.score(x, y)
alpha = model.intercept_
beta_1 = model.coef_[0]
beta_2 = model.coef_[1]
beta_3 = model.coef_[2]
beta_3 = model.coef_[3]
beta_4 = model.coef_[4]

