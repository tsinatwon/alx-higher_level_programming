#!/usr/bin/python3

''' modul 2_ rectangle
this is a rectangle class
'''


class Rectangle:
    """
    this is rectangle class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        """Return the printable representation of the Rectangle.
            Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
        claculate the area of  rectangle
    """
    def area(self):
        return self.__width * self.__height

    """
        claculate the perimeter
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __repr__(self):
        '''
            returnn formal string
        '''
        rect = "Rectangle( " + str(self.__width) + ", " + \
               str(self.__height) + ")"
        return rect
