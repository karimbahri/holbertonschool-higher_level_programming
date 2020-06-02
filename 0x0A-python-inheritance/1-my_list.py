#!/usr/bin/python3
"""
    my_list:
        classes:
            MyList
"""


class MyList(list):
    """MyList: inherits from list"""
    def print_sorted(self):
        """print_sorted: ascending sort"""

        print(sorted(self))
