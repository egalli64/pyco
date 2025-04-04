"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Log and Test

The unittest module
"""

import unittest

from p6.m1_robustness.s7_testing import e1_math as m


class TestS7Math(unittest.TestCase):
    def test_add_plain(self):
        expected = 42
        actual = m.add(2, 40)
        self.assertEqual(actual, expected)

    def test_subtract_plain(self):
        self.assertEqual(m.subtract(50, 8), 42)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            m.floor_divide(10, 0)
