#!/usr/bin/python3
"""A function that checks if object is a subclass of another object"""


def inherits_from(obj, a_class):
    """Return True if obj is a subclass of a_class"""
    return type(obj) != a_class and isinstance(obj, a_class)
