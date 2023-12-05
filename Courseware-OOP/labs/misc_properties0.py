# misc_properties1.py

import math


class Point:
    """
    class Point has been constructed to expose the attributes
    "x" and "y" to the public.

    @property was employed to the attributes with the foresight that the future
    may hold the changing of internal implementation of a given attribute.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def hypotenuse(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


point1 = Point(1, 1)

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print("")

point1.x = 3
point1.y = 4

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print("")

print(f"hypotenuse = {point1.hypotenuse()}")
print("")

point2 = Point(2, 2)

print(f"x = {point2.x}")
print(f"y = {point2.y}")
print("")

point2.x = 13
point2.y = 15

print(f"x = {point2.x}")
print(f"y = {point2.y}")
print("")
