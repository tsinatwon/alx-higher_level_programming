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
