#!/usr/bin/python3
class Square:
    """A class that defines a square by its size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Return a string representation of the square"""
        if self.__size == 0:
            return ""
        else:
            result = "\n" * self.__position[1]
            for i in range(self.__size):
                result += " " * self.__position[0]
                result += "#" * self.__size
                if i < self.__size - 1:
                    result += "\n"
            return result
