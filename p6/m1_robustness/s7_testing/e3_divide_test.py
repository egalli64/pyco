"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

The unittest module - assertRaises()
"""

import unittest
import e1_math as m


class TestMathFloorDivide(unittest.TestCase):
    def test_divide_plain(self):
        expected = 42
        actual = m.floor_divide(84, 2)
        self.assertEqual(actual, expected)

    def test_divide_zero(self):
        # the check is done implicity in __exit__, called by "with"
        # if no exception is raised, the test fails
        # otherwise the exception is stored in the context
        with self.assertRaises(ZeroDivisionError) as context:
            m.floor_divide(10, 0)

        # if the exception has been raised, it is stored in the context
        self.assertEqual(str(context.exception), "integer division or modulo by zero")


if __name__ == "__main__":
    unittest.main()
