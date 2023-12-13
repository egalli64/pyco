"""
Python Course

https://github.com/egalli64/pyco

Module 11 - Log and Test

The unittest module
"""
import unittest


class MathTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertAlmostEqual(3.0 - 2.1, 0.9, places=15)

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            10 / 0


if __name__ == "__main__":
    unittest.main()
