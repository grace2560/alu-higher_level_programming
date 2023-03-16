#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""

    def __init__(self, width=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            width (int): The width of the new square.
            position (int, int): The position of the new square.
        """
        self.width = width
        self.height =height

    @property
    def width(self):
        """Get/set the current size of the square."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("height must be a tuple of 2 positive integers")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle."""
        return (self.__width * self.__width)

    def my_print(self):
        """Print the rectangle with the # character."""
        if self.__width == 0:
            print("")
            return

        [print("") for i in range(0, self.__height[1])]
        for i in range(0, self.__width):
            [print(" ", end="") for j in range(0, self._height[0])]
            [print("#", end="") for k in range(0, self._width)]
            print("")

