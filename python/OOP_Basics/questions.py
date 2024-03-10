class Person:
    pass

a = Person()
b = Person()
print(a==b)

class X:
    """Example Class"""
    count = 0
    avg = 0
    def __init__(self):
        """init function for class X"""
        self.a = 1
        self.b = 2


x = X()
x.z = 4
print(x.a, x.b, x.z)
