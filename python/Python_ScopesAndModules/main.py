import os
import sys
import areas
"""
This module is exercises of the Scopes and Modules Worksheet:

CR: Denis Vilanevsky
"""

# exercise1:
ziv = 1


def check_global_name(name):
    """
    check if a given name is defined in the global namespace
    :param name: any name of variable
    :type name: string
    :return: if it's in the global namespace
    :rtype: boolean
    """
    return str(name) in globals()


print("is in globals? ", check_global_name("ziv"))
print(globals())

print("-----------------------------------------------")

# exercise2:
# using the module areas 
print(areas.circle_area(20))
print(areas.triangle_area(20, 10))
print(areas.rectangle_area(20, 10))

print("-----------------------------------------------")

# exercise3:
# print the name of the system, logged in user, working directory
print(os.name)
print(os.getlogin())
print(os.getcwd())

print("-----------------------------------------------")

# exercise4:
# receive command line arguments and print them in reverse order
print(sys.argv[::-1])

print(globals())

