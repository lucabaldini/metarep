import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline


class ProbabilityDensityDistribution(InterpolatedUnivariateSpline):

    def __init__(self, x, y):
        spline = InterpolatedUnivariateSpline(x, y)
        norm = spline.integral(x.min(), x.max())
        self._x = x
        self._y = y / norm
        super().__init__(self._x, self._y)

    def plot(self):
        plt.plot(self._x, self._y, 'o')
        x = np.linspace(self._x.min(), self._x.max(), 250)
        plt.plot(x, self(x))

    def normalization(self):
        return self.integral(self._x.min(), self._x.max())
    
    def integrate(self, x1, x2):
        return self.integral(x1, x2)




if __name__ == '__main__':
    x = np.linspace(0., 1., 4)
    y = np.exp(x)
    pdf = ProbabilityDensityDistribution(x, y)
    
    x0 = 0.5
    print(np.exp(x0), pdf(x0)) #InterpolateUnivariateSpline has a __call__ method
    print(pdf.normalization())

    #UT: evaluate the probability of the random variable to be on a given interval
    x1 = 0
    x2 = 1
    print(pdf.integrate(x1, x2))

    pdf.plot()
    plt.show()
