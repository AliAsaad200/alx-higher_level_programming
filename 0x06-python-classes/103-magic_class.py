#!/usr/bin/python3
"""Module to define a MagicClass"""


class MagicClass:
    """MagicClass class"""

    def __init__(self, radius=0):
        """Initialization method with optional radius parameter"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Method to calculate the area of the circle"""
        return self.__radius ** 2 * 3.14159265359

    def circumference(self):
        """Method to calculate the circumference of the circle"""
        return 2 * 3.14159265359 * self.__radius
