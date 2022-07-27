#!/usr/bin/python3
"""  squae class"""


class Square:
    """class square with attribute size"""

    def __init__(self, size=0):
        """ intialize the square class"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """returns  private instance size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """" sets the size of private atrribute"""
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()
