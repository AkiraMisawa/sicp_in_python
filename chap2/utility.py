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
    :type x: FunctionType | None
    :rtype: object | FunctionType
    """
    if x is None:
        return None
    else:
        return x(lambda a, b: a)


def cdr(x):
    """
    :type x: FunctionType | None
    :rtype: object | FunctionType
    """
    if x is None:
        return None
    else:
        return x(lambda a, b: b)


# noinspection PyShadowingBuiltins
def list(*x):
    """
    :type x: object
    :rtype: FunctionType | None
    """
    def list_iter(*y, b):
        """
        :type y: object
        :type b: object
        :rtype: FunctionType | None
        """
        if len(y) == 0:
            return None
        elif len(y) == 1:
            a = y[0]
            return cons(a, b)
        else:
            a = y[-1]
            z = y[:-1]
            return list_iter(*z, b=cons(a, b))

    return list_iter(*x, b=None)


def is_null(items):
    """
    :type items: FunctionType | None
    :rtype: boll
    """
    return items is None


def length(items):
    """
    :type items: FunctionType | None
    :rtype: int
    """
    def length_iter(a, count):
        """
        :type a: FunctionType | None
        :type count: int
        :rtype: int
        """
        if is_null(a):
            return count
        else:
            return length_iter(cdr(a), count + 1)

    return length_iter(items, 0)


def list_ref(items, n):
    """
    :type items: FunctionType
    :type n: int
    :rtype: object
    """
    def list_ref_iter(x, count):
        """
        :type x: FunctionType
        :type count: int
        :rtype: FunctionType | object
        """
        if count == 0:
            return car(x)
        else:
            return list_ref_iter(cdr(x), count - 1)

    if is_null(items):
        raise ValueError('empty list')
    items_length = length(items)
    if n < 0:
        n += items_length
    if n >= items_length or n < 0:
        raise ValueError('list index out of range')
    return list_ref_iter(items, n)


def list_to_str(l):
    def one_element_to_str(l):
        if callable(car(l)):
            return list_to_str(car(l)) + ' '
        else:
            return str(car(l)) + ' '

    def to_str_impl(l):
        string = ''
        if not is_null(l):
            if length(l) > 0:
                string = one_element_to_str(l)
            if length(l) > 1:
                string = string + to_str_impl(cdr(l))
        return string

    return '( ' + to_str_impl(l) + ')'


def print_list(l):
    print(list_to_str(l))


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
        self.assertEqual(c, car(cdr(cdr(x))))

    def test_case_5(self):
        x = list()
        y = list(1, 2, 3)
        self.assertEqual(0, length(x))
        self.assertEqual(3, length(y))

    def test_case_6(self):
        a = 1
        b = 2
        c = 3
        x = list(a, b, c)
        self.assertEqual(a, list_ref(x, 0))
        self.assertEqual(c, list_ref(x, -1))

    def test_case_9(self):
        a = list()
        b = list(1)
        c = list(1, 2)
        d = list(3, 4)
        e = list(1, 2, d)
        f = list(7, e, d)
        self.assertEqual(list_to_str(a), '( )')
        self.assertEqual(list_to_str(b), '( 1 )')
        self.assertEqual(list_to_str(list(b)), '( ( 1 ) )')
        self.assertEqual(list_to_str(c), '( 1 2 )')
        self.assertEqual(list_to_str(e), '( 1 2 ( 3 4 ) )')
        self.assertEqual(list_to_str(f),
                         '( 7 ( 1 2 ( 3 4 ) ) ( 3 4 ) )')


if __name__ == '__main__':
    unittest.main()
