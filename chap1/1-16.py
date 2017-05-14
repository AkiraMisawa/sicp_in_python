# -*- coding: utf-8 -*-
import unittest
import math


def fast_expt2(b, n):
    def is_even(x): return x % 2 == 0

    def square(x): return x * x

    def fast_expt_iter(a, b, n):
        """
        a * b^n: const.
        """
        if n == 0:
            return a
        if is_even(n):
            return fast_expt_iter(a, square(b), n / 2)
        else:
            return fast_expt_iter(a * b, b, n - 1)

    return fast_expt_iter(1, b, n)


class ExponentialTest2(unittest.TestCase):
    def test_case0(self):
        self.assertEqual(math.pow(4, 0), fast_expt2(4, 0))

    def test_case1(self):
        self.assertEqual(math.pow(2, 10), fast_expt2(2, 10))

    def test_case2(self):
        self.assertEqual(math.pow(3, 5), fast_expt2(3, 5))


if __name__ == '__main__':
    print(fast_expt2(4, 0))
    print(fast_expt2(2, 10))
    print(fast_expt2(3, 5))
    unittest.main()
