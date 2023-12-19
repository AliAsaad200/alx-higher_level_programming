#!/usr/bin/python3
"""Module to define a Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method with optional size and position parameters"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square with '#' characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Method to return a string representation of the square"""
        result = ""
        if self.__size == 0:
            return result
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
            return result[:-1]
    