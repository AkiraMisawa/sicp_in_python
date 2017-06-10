# -*- coding: utf-8 -*-
import unittest


def fib(n):
    def is_even(x): return x % 2 == 0

    def square(x): return x * x

    def fib_logscale_iter(a, b, p, q, count):
        if count == 0:
            return b
        elif is_even(count):
            """
            p' := p^2 + q^2
            q' := 2pq + q^2
            """
            pprime = square(p) + square(q)
            qprime = 2 * p * q + square(q)
            return fib_logscale_iter(a, b, pprime, qprime, count / 2)
        else:
            first = b * q + a * q + a * p
            second = b * p + a * q
            return fib_logscale_iter(first, second, p, q, count - 1)

    return fib_logscale_iter(1, 0, 0, 1, n)


class FibLogScaleTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(0, fib(0))

    def test_case2(self):
        self.assertEqual(1, fib(2))

    def test_case3(self):
        self.assertEqual(8, fib(6))

    def test_case4(self):
        self.assertEqual(55, fib(10))

    def test_case5(self):
        self.assertEqual(4181, fib(19))


if __name__ == '__main__':
    unittest.main()
