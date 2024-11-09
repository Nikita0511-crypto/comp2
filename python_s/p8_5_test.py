import unittest

from p8_5_main import *

class Mytest(unittest. TestCase):

    def test_arg(self):
        self.assertEqual(adder(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=21), 31)

    def test_mixed(self):
        self.assertEqual(adder(5, b=3), 8)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, y, a=x), 5)

    def test_wrong_datatype(self):
        self.assertEqual(adder("5", "abs", 10), 15)

        if __name__ == "__main__":
            unittest.main()
