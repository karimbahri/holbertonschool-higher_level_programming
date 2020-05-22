#!/usr/bin/python3
import unittest
max = __import__("6-max_integer").max_integer
"""
    6-max_integer_test: unit test file
"""


class test_max_integer(unittest.TestCase):
    """
        test_max_integer: test all cases of max_integer
    """
    def test_cases(self):
        """
            test_cases: attribute
        """
        self.assertEqual(max([10, 2, 9, 30, 21]), 30)
        self.assertEqual(max([]), None)
        self.assertEqual(max(), None)
        self.assertEqual(max("Konnichiwa"), 'w')
        self.assertEqual(max([-8, -3]), -3)
        self.assertEqual(max(""), None)
