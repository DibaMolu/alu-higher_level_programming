#!/usr/bin/python3
''' defined class Mylist that inherites.'''


class Mylist(list):
        '''Implements the sorted printing .'''

            def print_sorted(self):
                        '''print a list in sorted order.'''
                                print(sorted(self))
