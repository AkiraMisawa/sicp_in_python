# -*- coding: utf-8 -*-
"""for utility functions"""

import unittest
from types import FunctionType


def cons(a, b):
    """
    :type a: object
    :type b: object
    :rtype: FunctionType
    """
    return lambda x: x(a, b)


def car(x):
    """
    :type x: FunctionType
    :rtype: object | FunctionType
    """
    return x(lambda a, b: a)


def cdr(x):
    """
    :type x: FunctionType
    :rtype: object | FunctionType
    """
    return x(lambda a, b: b)


def print_cons(x):
    print("(", car(x), ",", cdr(x), ")")


# noinspection PyShadowingBuiltins
def list(*x):
    """
    :type x:
    :rtype: FunctionType
    """
    if len(x) == 0:
        return cons(None, None)
    elif len(x) == 1:
        return cons(x[0], None)
    else:
        a = x[-2]
        b = x[-1]
        z = x[:-2]
        if z:
            return list(*z, cons(a, b))
        else:
            return cons(a, b)


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case_1(self):
        a = 1
        b = 2
        x = cons(a, b)
        self.assertEqual(a, car(x))
        self.assertEqual(b, cdr(x))

    def test_case_2(self):
        x = list()
        self.assertEqual(None, car(x))
        self.assertEqual(None, cdr(x))

    def test_case_3(self):
        a = 1
        x = list(a)
        self.assertEqual(a, car(x))
        self.assertEqual(None, cdr(x))

    def test_case_4(self):
        a = 1
        b = 2
        c = 3
        x = list(a, b, c)
        self.assertEqual(a, car(x))
        self.assertEqual(b, car(cdr(x)))
        self.assertEqual(c, cdr(cdr(x)))


if __name__ == '__main__':
    unittest.main()
