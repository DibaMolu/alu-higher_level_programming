#!/usr/bin/python3
"""A function that write into a file"""


def write_file(filename="", text=""):
    """write a file"""

    with open(filename, "w") as file:
        return file.write(text)
