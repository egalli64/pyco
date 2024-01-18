"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 5 - Log and Test

The unittest module - assertNotEqual(), assertAlmostEqual()
"""
import unittest
import s5a_math as m


class TestMathSubtract(unittest.TestCase):
    """Tests written in a compact way"""

    def test_subtract_plain(self):
        self.assertEqual(m.subtract(50, 8), 42)

    def test_subtract_precision(self):
        """3.0 - 2.1 is _not_ equal to 0.9!"""
        self.assertNotEqual(m.subtract(3.0, 2.1), 0.9)

    def test_subtract_close_places(self):
        """3.0 - 2.1 is very close to 0.9, but increase the number of decimal places and the test fails"""
        self.assertAlmostEqual(m.subtract(3.0, 2.1), 0.9, places=15)

    def test_subtract_close_delta(self):
        """3.0 - 2.1 is very close to 0.9, but decrease the delta and the test fails"""
        self.assertAlmostEqual(m.subtract(3.0, 2.1), 0.9, delta=2e-16)


if __name__ == "__main__":
    unittest.main()
