import os
import sys
import areas


# exercise1:
ziv = 1


def check_global_name(name):
    return str(name) in globals()


print("is in globals? ", check_global_name("ziv"))
print(globals())

print("-----------------------------------------------")

# exercise2:
print(areas.circle_area(20))
print(areas.triangle_area(20, 10))
print(areas.rectangle_area(20, 10))

print("-----------------------------------------------")

# exercise3:
print(os.name)
print(os.getlogin())
print(os.getcwd())

print("-----------------------------------------------")

# exercise4:
print(sys.argv[::-1])

