#!/usr/bin/python3
"""100-my_int:
        classes: MyInt
"""


class MyInt(int):
    """MyInt inherits from int"""

    def __eq__(self, comparator):
        """eq: not equal function"""
        result = supper().__int__ != comparator
        return result

    def __ne__(self, comparator):
        """ne: equal function"""
        result = super().__int__ == comparator
        return result
