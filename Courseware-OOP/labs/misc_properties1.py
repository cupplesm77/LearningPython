# misc_properties1.py

import math


class Point:
    """
    class Point has been refactored to expose the attributes
    "r" and "p" to the public rather than "x" and "y"

    @property was employed to the attributes with the foresight that the future
    may hold the changing of internal implementation of a given attribute.
    """

    def __init__(self, x, y):
        try:
            self._x = float(x)
            print("Validated")
        except ValueError:
            raise ValueError('"x" must be a real number') from None
        try:
            self._y = float(y)
            print("Validated")
        except ValueError:
            raise ValueError('"y" must be a real number') from None
        self._p = x + y
        self._q = y - x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated")
        except ValueError:
            raise ValueError('"x" must be a number') from None
        self._p = self._x + self._y
        self._q = self._y - self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated")
        except ValueError:
            raise ValueError('"y" must be a number') from None
        self._p = self._x + self._y
        self._q = self._y - self._x

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        try:
            self._p = float(value)
            print("Validated")
        except ValueError:
            raise ValueError('"p" must be a number') from None
        self._x = (self._p - self._q) / 2.0
        self._y = (self._p + self._q) / 2.0

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, value):
        try:
            self._q = float(value)
            print("Validated")
        except ValueError:
            raise ValueError('"q" must be a number') from None
        self._x = (self._p - self._q) / 2.0
        self._y = (self._p + self._q) / 2.0

    def hypotenuse(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


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

print(f"hypotenuse = {point1.hypotenuse()}")
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
