import numpy
from sklearn.linear_model import LinearRegression

# create data
x = [[0,1],
    [5, 1],
    [15, 2],
    [25, 5],
    [35, 11],
    [45, 15],
    [55, 34],
    [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = numpy.array(x), numpy.array(y)

# create model
model = LinearRegression().fit(x, y)

# retrieve score
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept', model.intercept_)
print('slope', model.coef_)
