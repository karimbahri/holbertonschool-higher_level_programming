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

        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 9)

        with self.assertRaises(ValueError):
            rect = Rectangle(9, 0)

        with self.assertRaises(TypeError):
            rect = Rectangle("holberton", 9)

        with self.assertRaises(TypeError):
            rect = Rectangle(9, "holberton")

        with self.assertRaises(ValueError):
            rect = Rectangle(9, 9, -3)

        with self.assertRaises(ValueError):
            rect = Rectangle(9, 9, 10, -1)

        rect = Rectangle(2, 2)
        self.assertEqual(rect.area(), 4)
        self.assertEqual(str(rect), "[Rectangle] (10) 0/0 - 2/2")
