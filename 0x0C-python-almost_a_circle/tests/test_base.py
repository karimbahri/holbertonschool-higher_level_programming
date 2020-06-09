#!/usr/bin/python3
"""unit tests"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """class that inherits from TestCase"""
    def testes(self):
        """test function"""
        base = Base()
        self.assertEqual(base.id, 1)
        #--------------TEST1---------------------
        base1 = Base()
        self.assertEqual(base1.id, 2)
        #--------------TEST2---------------------
        base2 = Base(14)
        self.assertEqual(base2.id, 14)
