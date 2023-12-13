"""
Python Course

https://github.com/egalli64/pyco

Module 11 - Log and Test

The unittest module
"""
import unittest
import s5_math as m


class TestMathAdd(unittest.TestCase):
    """Stress on readability"""

    def test_add_plain(self):
        expected = 42
        actual = m.add(2, 40)
        self.assertEqual(actual, expected)

    def test_add_zero(self):
        expected = 2
        actual = m.add(2, 0)
        self.assertEqual(actual, expected)

    def test_add_zero_zero(self):
        expected = 0
        actual = m.add(0, 0)
        self.assertEqual(actual, expected)

    def test_add_negative(self):
        expected = -42
        actual = m.add(-10, -32)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
