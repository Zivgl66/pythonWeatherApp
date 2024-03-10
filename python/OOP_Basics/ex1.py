from math import sqrt


class Point:

    def __init__(self, x=0.0, y=0.0):
        if self.check_number(x) and self.check_number(y):
            self.x = x
            self.y = y
        else:
            raise Exception("Sorry, X and Y need to be Numbers")

    def check_number(self, z):
        return isinstance(z, (int, float)) and not isinstance(z, bool)

    def distance_from_origin(self):
        return sqrt(self.x ** 2 + self.y ** 2)


p = Point(1, 2)
print(p.x)
