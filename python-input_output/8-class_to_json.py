#!/usr/bin/python3
"""A function that returns a dictionary description"""


def class_to_json(obj):
    """Return a dictionary description of an object"""
    return obj.__dict__
