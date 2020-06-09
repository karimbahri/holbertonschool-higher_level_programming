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
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.id, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        rect1 = Rectangle(5, 4, 10, 19, 44)
        self.assertEqual(rect1.x, 10)
        self.assertEqual(rect1.y, 19)
        self.assertEqual(rect1.id, 44)
