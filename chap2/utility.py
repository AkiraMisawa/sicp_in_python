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


def is_list(x):
    return callable(x)


def is_same_list(lst1, lst2):
    def is_same_element(x1, x2):
        if is_list(x1) == is_list(x2):
            if is_list(x1):
                return is_same_list(x1, x2)
            else:
                return x1 == x2
        else:
            return False

    if length(lst1) != length(lst2):
        return False
    elif length(lst1) == 0:
        return True
    else:
        is_same_car = is_same_element(car(lst1), car(lst2))
        is_same_cdr = is_same_list(cdr(lst1), cdr(lst2))
        return is_same_car and is_same_cdr


def append(list1, list2):
    """
    :type list1: FunctionType | None
    :type list2: FunctionType | None
    :rtype: FunctionType | None
    """
    if is_null(list1):
        return list2
    else:
        return cons(car(list1), append(cdr(list1), list2))


# noinspection PyShadowingBuiltins
def map(proc, items):
    """
    :type proc: FunctionType
    :type items: FunctionType | None
    :rtype: FunctionType | None
    """
    if is_null(items):
        return
    else:
        return cons(proc(car(items)), map(proc, cdr(items)))


def list_to_str(lst):
    def one_element_to_str(x):
        if is_list(x):
            return list_to_str(x) + ' '
        else:
            return str(x) + ' '

    def to_str_impl(lst):
        if not is_null(lst):
            return one_element_to_str(car(lst)) + to_str_impl(cdr(lst))
        else:
            return ''

    return '( ' + to_str_impl(lst) + ')'


def print_list(lst):
    print(list_to_str(lst))


def print_cons(lst):
    print('( ' + str(car(lst)) + ' ' + str(cdr(lst)) + ' )')


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

    def test_case_7(self):
        list1 = list(1, 2, 3)
        list2 = list(1, 2, 3)
        list12 = list(list1, list2)
        list21 = list(list2, list1)
        list3 = list(list(1, 2, 3), list(1, 2, 3))
        self.assertTrue(is_same_list(list1, list2))
        self.assertTrue(is_same_list(list12, list21))
        self.assertTrue(is_same_list(list12, list3))

    def test_case_8(self):
        x = list(1, 2, 3)
        x_map = map(lambda i: 2 * i, x)
        y = list(2, 4, 6)
        self.assertTrue(is_same_list(x_map, y))

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
