# misc_properties1.py

import math


class Point:
    """
    class Point has been refactored to expose the attributes
    "r" and "p" to the public;  "x" and "y" remain available as well.

    @property was employed to the attributes with the foresight that the future
    may hold the changing of internal implementation of a given attribute.

    functional relationship between x,y and p,q:
    p = x + y
    q = y - x

    x = (p - q) / 2.0
    y = (p + q) / 2.0

    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ******* x getter and setter
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)   # float already has an associated exception

    # ******* y getter and setter
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = float(value)   # float already has an associated exception


    # ******* p getter and setter
    @property
    def p(self):
        return self.x + self.y

    @p.setter
    def p(self, value):
        self._p = float(value)
        self.x = (value - self.q) / 2.0
        self.y = (value + self.q) / 2.0


    # ******* q getter and setter
    @property
    def q(self):
        return self.y - self.x

    @q.setter
    def q(self, value):
        self._q = float(value)
        self.x = (self.p - value) / 2.0
        self.y = (self.p + value) / 2.0


    # ******* instance methods
    def hypotenuse(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

# ******* Test cases *********************************
point1 = Point(1, 1)

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print("")
print(f"point1.p = {point1.p}")
print(f"point1.q = {point1.q}")
print("")

point1.x = 3
point1.y = 4

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print("")
print(f"point1.p = {point1.p}")
print(f"point1.q = {point1.q}")
print("")

print(f"hypotenuse for point1 = {point1.hypotenuse()}")
print("")

point2 = Point(2, 2)

print(f"x = {point2.x}")
print(f"y = {point2.y}")
print("")
print(f"point2.p = {point2.p}")
print(f"point2.q = {point2.q}")
print("")

point2.x = 100
point2.y = 99

print(f"x = {point2.x}")
print(f"y = {point2.y}")
print("")
print(f"point2.p = {point2.p}")
print(f"point2.q = {point2.q}")
print("")

print(f"hypotenuse for point2 = {point2.hypotenuse()}")
print("")