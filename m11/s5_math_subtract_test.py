"""
Python Course

https://github.com/egalli64/pyco

Module 11 - Log and Test

The unittest module
"""
import unittest
import s5_math as m


class TestS4Math(unittest.TestCase):
    """Stress on compactness"""

    def test_subtract_plain(self):
        self.assertEqual(m.subtract(50, 8), 42)

    def test_subtract_precision(self):
        """3.0 - 2.1 is _not_ equal to 0.9!"""
        self.assertNotEqual(m.subtract(3.0, 2.1), 0.9)

    def test_subtract_close_enough(self):
        """3.0 - 2.1 is very close to 0.9!"""
        self.assertAlmostEqual(m.subtract(3.0, 2.1), 0.9, places=15)


if __name__ == "__main__":
    unittest.main()
