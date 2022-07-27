#!/usr/bin/python3
"""  squae class"""


class Square:
    """class square with attribute size"""

    def __init__(self, size=0, postion=(0, 0)):
        """ intialize the square class"""
        self.size = size
        self.postion = postion

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
            prints the square with character #
        """
        if self.__size == 0:
            print()
        else:
            i, j = 0, 0
            temp = self.__postion[0]
            for i in range(self.__postion[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * temp, "#" * self.__size))

    @property
    def postion(self):
        """return the private attribute  postion"""
        return (self.__postion)

    @postion.setter
    def postion(self, coordinate):
        """ sets value for postion coordinate"""
        if not isinstance(coordinate, tuple) or len(coordinate) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(2):
            if coordinate[i] < 0:
                raise TypeError("position \
                                must be a tuple of 2 positive integers")
        self.__postion = coordinate
