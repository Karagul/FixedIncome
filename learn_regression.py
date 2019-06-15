import numpy
from sklearn.linear_model import LinearRegression

x = numpy.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y = numpy.array([5, 20, 14, 32, 22, 38])

model = LinearRegression().fit(x, y)
