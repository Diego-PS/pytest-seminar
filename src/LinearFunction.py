import math

class LinearFunction:
    def __init__(self, a: float, b: float):
        if math.isclose(a, 0):
            raise Exception("Not a valid linear function, value of 'a' cannot be zero") 
        self.a = a
        self.b = b

    def calculate(self, x: float):
        a, b = self.a, self.b
        return a*x + b
    
    def root(self):
        a, b = self.a, self.b
        return -b/a