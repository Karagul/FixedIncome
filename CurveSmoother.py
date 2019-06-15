import numpy
from sklearn.linear_model import LinearRegression

class CurveSmoother():
    """ a simple curve smoothing model """

    def __init__(self, y_data=[], **kwargs):
        self.y_data = [float(x) for x in y_data]
        self.x_data = []
        self.alpha = 0
        self.betas = []
        self.beta_count = 0
        for key, value in kwargs.items():
            self.x_data.append(value)
            self.beta_count += 1
        self.y = self.y_data
        
        self.x = []
        i = 0
        while (i < len(self.y)):
            row = []
            j = 0
            while (j < len(self.x_data)):
                row.append(self.x_data[j][i])
                j += 1
            self.x.append(row)
            i += 1
        
        self.x, self.y = numpy.array(self.x), numpy.array(self.y)

    def smooth(self):
        model = LinearRegression().fit(self.x, self.y)
        self.alpha = model.intercept_
        i = 0
        while (i < self.beta_count):
            self.betas.append(model.coef_[i])
            i += 1
        return [self.alpha, self.betas]

