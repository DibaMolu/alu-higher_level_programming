#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

     def __init__(self, size=0, position=(0, 0)):
         """Initialize a new square.

         Args:
             size (int): The size of the square.
         """
         if isinstance(size, int) is not True:
             raise TypeError("size must be an integer")
         elif size < 0:
             raise ValueError("size must be >=0")

         if (isinstance(position, tuple) is not True or
                 len(position) != 2 or
                 not all(isinstance(num, int) for num in position) or
                 not all(num >= 0 for num in position)):
             raise TypeError("position must be a tuple of 2 positive integers")
         self.__size = size
         self.__position = position

         def area(self):
             """Return the area of the square."""

             return self.__size ** 2

         @property
         def size(self):
             """Return the size of the square."""

             return self.__size

         @size.setter
         def size(slf, value):
             """Set the size of the square.

             Args:
                 value (int): The size of the square.
             """
             if isinstance(value, int) is not True:
                 raise TypeError("size must be an integer")
             elif value < 0:
                 raise ValueError("size must be >=0")
             self.__size = value

         @property
         def position(self):
             """Return the position of the square
