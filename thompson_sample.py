import random
import math

class Normal:
    def __init__(self, mean, stdev=1.0):
        self.mean = mean
        self.stdev = stdev

    def sample(self):
        return random.normalvariate(self.mean, self.stdev)

    
class Beta:
    def __init__(self):
        self.alpha = 1
        self.beta = 1

    @property
    def success(self):
        self.alpha += 1

    @property
    def failure(self):
        self.beta += 1

    def mean(self):
        return self.alpha / (self.alpha + self.beta)

    def stdev(self):
        return math.sqrt(self.alpha * self.beta / ((self.alpha + self.beta)**2 
                                                   * (self.alpha + self.beta + 1)))

    def sample(self):
        return random.betavariate(self.alpha, self.beta)
