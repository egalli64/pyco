"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Log and Test

The unittest module - assertEqual()
"""
import unittest
import e1_math as m


class TestMathAdd(unittest.TestCase):
    """A simple test case"""

    def test_add_plain_true(self):
        """Using assertTrue(), top flexibility"""
        expected = 42
        actual = m.add(2, 40)
        self.assertTrue(actual == expected)

    def test_add_plain_equal(self):
        """Using assertEqual(), usually more readable"""
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
