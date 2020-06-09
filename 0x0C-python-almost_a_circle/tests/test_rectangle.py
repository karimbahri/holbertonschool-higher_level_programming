#!/usr/bin/python3
"""unit tests"""
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """class that inherits from TestCase"""
    def test_cases(self):
        """function test"""
        rect = Rectangle(5, 4)
        self.assertEqual(rect.width, 5)
