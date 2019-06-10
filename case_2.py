import csv
import matplotlib.pyplot as plt
from DescriptiveStats import DescriptiveStats
from datetime import datetime

## TODO: FIX SHARPE RATIO CALCULATION

rfr = .0020
initial_investment = 100.00

# extract
with open("case_2.csv") as f:
    mkt_data = []
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        mkt_data.append(row)

# transform
i = 0
dates = []
p_px = []
s_px = []
while (i < len(mkt_data)):
    dates.append(datetime.strptime(mkt_data[i][0], '%m/%d/%Y'))
    p_px.append(float(mkt_data[i][1]))
    s_px.append(float(mkt_data[i][2]))
    i += 1

# assign initial share value
p_shares = 100 / p_px[0]
s_shares = 100 / s_px[0]

# compute day-end values
p_value = []
s_value = []
t_value = []
i = 0
while (i < len(dates)):
    p_value.append(p_px[i] * p_shares)
    s_value.append(s_px[i] * s_shares)
    t_value.append(p_value[i] - s_value[i])
    i += 1

# compute daily returns
p_percent = []
s_percent = []
p_percent.append(0)
s_percent.append(0)
i = 1
while (i < len(dates)):
    if (i > 0):
        p_percent.append(p_px[i] / p_px[i-1] - 1)
        s_percent.append(s_px[i] / s_px[i-1] - 1)
    i += 1

# print data
i = 0
while (i < len(dates)):
    print(str(dates[i]), str(round(p_px[i],2)), str(round(s_px[i],2)), str(round(p_value[i],2)),
            str(round(s_value[i],2)), str(round(p_percent[i],4)), str(round(s_percent[i],4)),
            str(round(t_value[i],2)))
    i += 1

# print chart
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, t_value, c='red')
plt.title("Portfolio Value", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("$", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# print analysis
realized_returns = t_value[len(t_value)-1] / 5
excess_returns = realized_returns - rfr
print("r:", str(round(excess_returns,4)))
des_set = DescriptiveStats(t_value)
t_sigma = des_set.sample_standard_deviation() / 5
print("Sigma: ", str(round(t_sigma,4)))
sharpe = excess_returns / t_sigma
print("Sharpe: ", str(round(sharpe,2)))

plt.show()
