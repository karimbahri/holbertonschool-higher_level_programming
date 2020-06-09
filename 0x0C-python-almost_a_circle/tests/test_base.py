#!/usr/bin/python3
"""unit tests"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """class that inherits from TestCase"""
    def test_cases(self):
        """test function"""
        base = Base()
        self.assertEqual(base.id, 1)

        base1 = Base()
        self.assertEqual(base1.id, 2)

        base2 = Base(14)
        self.assertEqual(base2.id, 14)
