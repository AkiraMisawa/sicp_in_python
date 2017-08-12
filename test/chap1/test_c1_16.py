import math
import unittest
import chap1.c1_16 as c1


class ExponentialTest2(unittest.TestCase):
    def test_case0(self):
        self.assertEqual(math.pow(4, 0), c1.fast_expt2(4, 0))

    def test_case1(self):
        self.assertEqual(math.pow(2, 10), c1.fast_expt2(2, 10))

    def test_case2(self):
        self.assertEqual(math.pow(3, 5), c1.fast_expt2(3, 5))


if __name__ == '__main__':
    unittest.main()
