"""
Python Course

https://github.com/egalli64/pyco

Module 11 - Log and Test

The unittest module
"""
import unittest
import s5_math as m


class TestMathFloorDivide(unittest.TestCase):
    def test_divide_plain(self):
        expected = 42
        actual = m.floor_divide(84, 2)
        self.assertEqual(actual, expected)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            m.floor_divide(10, 0)

        self.assertEqual(str(context.exception), "integer division or modulo by zero")


if __name__ == "__main__":
    unittest.main()
