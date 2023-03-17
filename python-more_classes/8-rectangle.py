#!/usr/bin/python3
"""creates class rectangle"""


class Rectangle:
    """defines initiation; width and height as private instance attributes"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """claculates and returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            elif rect_1.area() == rect_2.area():
                return rect_1

    def __str__(self):
        """prints rectangle shape using #"""
        rep_string = ""
        if self.__height > 0 and self.__width:
            for column in range(self.__height):
                for row in range(self.__width):
                    rep_string += str(self.print_symbol)
                rep_string += "\n"
            rep_string = rep_string[:-1]
            return rep_string
        else:
            return ""

    def __repr__(self) -> str:
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
