#!/usr/bin/python3
"""defined class Mylist that inherites the list of objects"""


class Mylist(list):
    """Represent a Mylist"""

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))
