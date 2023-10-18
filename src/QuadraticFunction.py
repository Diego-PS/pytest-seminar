import math
from typing import List
from .LinearFunction import LinearFunction

class QuadraticFunction:
    def __init__(self, a: float, b: float, c: float):
        if math.isclose(a, 0):
            raise Exception("Not a valid quadratic function, value of 'a' cannot be zero") 
        self.a = a
        self.b = b
        self.c = c

    def calculate(self, x: float) -> float:
        a, b, c = self.a, self.b, self.c
        return a*(x**2) + b*x + c

    def delta(self) -> float:
        a, b, c = self.a, self.b, self.c
        return b**2 - 4*a*c
    
    def roots(self) -> List[float]:
        delta = self.delta()
        delta_sqrt = delta**0.5
        print(delta_sqrt)
        a, b = self.a, self.b
        if math.isclose(delta, 0):
            return [-b/(2*a)]
        if delta < 0:
            return []
        return [(-b-delta_sqrt)/(2*a), (-b+delta_sqrt)/(2*a)]
    
    def derivative(self) -> LinearFunction:
        a, b = self.a, self.b
        return LinearFunction(2*a, b)