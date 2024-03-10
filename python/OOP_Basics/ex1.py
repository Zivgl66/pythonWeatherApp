from math import sqrt # imported for calculating sqrt
'''
    A Python module for a point (x and y). The point has 1 method of calculating the distance from a given other point
'''


class Point:

    def __init__(self, x=0.0, y=0.0):
        if self.check_number(x) and self.check_number(y):
            self.x = x
            self.y = y
        else:
            raise Exception("Sorry, X and Y need to be Numbers")

    def check_number(self, z):
        return isinstance(z, (int, float)) and not isinstance(z, bool)

    def distance_from_origin(self, Point):
        return sqrt((self.x - Point.x) ** 2 + (self.y - Point.y) ** 2)


p = Point(1, 2)
p2 = Point(10,20)
print(p.x)
print(p.distance_from_origin(p2))
