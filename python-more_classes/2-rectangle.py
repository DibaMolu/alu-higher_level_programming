#!/usr/bin/python3

'''module: 2-rectangle
This is a rectangle class.
'''


class Rectangle:
    '''class Rectangle this is an empty class
    '''

    def __init__(self, width=0, height=0):
        '''method: __init__
        initialize instance of Rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: set_width getter
        '''
        if (not isinstance(self.__width, int)) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >=0")
        return self.__width

    @width.setter
    def width(self, width):
        '''method: set_width setter
        '''
