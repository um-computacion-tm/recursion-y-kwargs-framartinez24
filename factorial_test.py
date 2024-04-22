import unittest
from factorial import *

class Testfactorial(unittest.TestCase):
    def test_1(self):
        result = factorial (1)
        self.assertEqual(result, 1)
    def test_2(self):
        result = factorial (2)
        self.assertEqual(result, 2)
    def test_5(self):
        result = factorial (5)
        self.assertEqual(result, 120)
    def test_10(self):
        result = factorial (10)
        self.assertEqual(result, 3628800)


if __name__ == '__main__':
    unittest.main()