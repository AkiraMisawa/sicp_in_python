# -*- coding: utf-8 -*-

import unittest


'''
アッカーマン関数を計算する
'''


def A(x, y):
    if y == 0:
        return 0
    if x == 0:
        return 2 * y
    if y == 1:
        return 2
    else:
        return A(x - 1, A(x, y - 1))


def f(n):
    '''
    f(n) := 2 * n
    '''
    return A(0, n)


def g(n):
    '''
    g(n) := 2^n
    '''
    return A(1, n)


def h(n):
    '''
    h(n) := 2^(2^(2^(2^(...))))
    2がどんどん(n層)べきべきになっていく
    '''
    return A(2, n)


def k(n):
    return 5 * n * n


class AckermanFunctionTest(unittest.TestCase):
    def test_case_A(self):
        self.assertEqual(1024, A(1, 10))
        self.assertEqual(65536, A(2, 4))
        self.assertEqual(65536, A(3, 3))

    def test_case_f(self):
        self.assertEqual(2, f(1))
        self.assertEqual(4, f(2))
        self.assertEqual(6, f(3))
        self.assertEqual(20, f(10))

    def test_case_g(self):
        self.assertEqual(2, g(1))
        self.assertEqual(4, g(2))
        self.assertEqual(256, g(8))
        self.assertEqual(1024, g(10))

    def test_case_h(self):
        self.assertEqual(2, h(1))
        self.assertEqual(4, h(2))
        self.assertEqual(16, h(3))
        self.assertEqual(65536, h(4))


if __name__ == '__main__':
    unittest.main()
