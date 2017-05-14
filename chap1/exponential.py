# -*- coding: utf-8 -*-
"""
in jsicp p.45
"""
import unittest
import math


def is_even(x):
    return x % 2 == 0


def square(x):
    return x * x


def recursive_pow(b, n):
    return 1 if n == 0 else b * recursive_pow(b, n - 1)


def recursive_pow2(b, n):
    def rec_pow_iter(product, counter):
        if counter > n:
            return product
        else:
            return rec_pow_iter(product * b, counter + 1)

    return rec_pow_iter(1, 1)


def fast_expt(b, n):
    if n == 0:
        return 1
    if is_even(n):
        temp = fast_expt(b, n / 2)
        return square(temp)
    else:
        return b * fast_expt(b, n - 1)


class ExponentialTest(unittest.TestCase):
    def test_case0(self):
        self.assertEqual(math.pow(4, 0), fast_expt(4, 0))

    def test_case1(self):
        self.assertEqual(math.pow(2, 10), fast_expt(2, 10))

    def test_case2(self):
        self.assertEqual(math.pow(3, 5), fast_expt(3, 5))


if __name__ == '__main__':
    print(recursive_pow(4, 0))
    print(recursive_pow(2, 10))
    print(recursive_pow(3, 5))
    print(recursive_pow2(4, 0))
    print(recursive_pow2(2, 10))
    print(recursive_pow2(3, 5))
    print(fast_expt(4, 0))
    print(fast_expt(2, 10))
    print(fast_expt(3, 5))
    unittest.main()
