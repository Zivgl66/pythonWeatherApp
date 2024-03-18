import math # Import math Library for pi


def circle_area(radius):
    """
    :param radius:  radius of a circle
    :type radius: float
    :return: calculation of a circle area
    :rtype: float
    """
    return math.pi * radius**2


def triangle_area(height, width):
    """
        :param height, width:  height and width of a triangle
        :type height: float
        :return: calculation of a triangle area
        :rtype: float
    """
    return 1/2 * width * height


def rectangle_area(width, height):
    """
           :param width, height:  width and height of a rectangle
           :type width: float
           :return: calculation of a rectangle area
           :rtype: float
    """
    return width * height
