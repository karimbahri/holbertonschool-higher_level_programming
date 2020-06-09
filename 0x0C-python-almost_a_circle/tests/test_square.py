#!/usr/bin/python3
"""unit tests"""
import unittest
from models.square import Square


class test_square(unittest.TestCase):
    """class that inherits from TestCase"""
    def test_cases(self):
        """function test"""
        sqr = Square(10)
        self.assertEqual(sqr.size, 10)
