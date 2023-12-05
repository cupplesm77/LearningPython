# misc_properties2.py

import math

DEG_2_RAD = math.pi / 180.0
RAD_2_DEG = 1.0 / DEG_2_RAD

class Point:
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
        self._r = math.sqrt(x * x + y * y)
        self._theta = math.atan2(y, x)


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
        self._r = math.sqrt(self._x * self._x + self._y * self._y)
        self._theta = math.atan2(self._y, self._x)


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
        self._r = math.sqrt(self._x * self._x + self._y * self._y)
        self._theta = math.atan2(self._y, self._x)


    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        try:
            self._r = float(value)
            print("Validated")
        except ValueError:
            raise ValueError('"r" must be a number') from None
        x = self._r * math.cos(DEG_2_RAD * self._theta)
        x = self._r * math.sin(DEG_2_RAD * self._theta)




    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, value):
        try:
            self._theta = float(value)
            print("Validated")
        except ValueError:
            raise ValueError('"theta" must be a number') from None
        x = self._r * math.cos(DEG_2_RAD * self._theta)
        x = self._r * math.sin(DEG_2_RAD * self._theta)



# instance 1
point1 = Point(1, 1)

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print("")
print(f"point1.r = {point1.r}")
print(f"point1.theta = {point1.theta * RAD_2_DEG}")
print("")

point1.x = 3
point1.y = 4

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print("")
print(f"point1.r = {point1.r}")
print(f"point1.theta = {point1.theta * RAD_2_DEG}")

print("")

# instance 2
point2 = Point(math.sqrt(2), math.sqrt(2))

print(f"x = {point2.x}")
print(f"y = {point2.y}")
print("")
print(f"point2.r = {point2.r}")
print(f"point2.theta = {point2.theta * RAD_2_DEG}")
print("")

point2.x = 6
point2.y = 8

print(f"x = {point2.x}")
print(f"y = {point2.y}")
print("")
print(f"point2.r = {point2.r}")
print(f"point2.theta = {point2.theta * RAD_2_DEG}")



