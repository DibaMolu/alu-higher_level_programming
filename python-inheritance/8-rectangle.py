#!/usr/bin/python3
"""A rectangle class that inherit from Geometry."""
BaseGeometry = __import__('7-base_geometry')BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height