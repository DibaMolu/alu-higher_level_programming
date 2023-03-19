#!/usr/bin/python3
"""A function that returns JSON representation of an object."""

import json


def to_json_string(my_obj):
    """converts an object to json"""
    return json.dumps(my_obj)
