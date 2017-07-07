# -*- coding: utf-8 -*-
"""2.20"""

import unittest


# noinspection PyUnresolvedReferences
from utility import cons, car, cdr, list, is_null, is_same_list


def is_even(x):
    """
    :type x: int
    :rtype: bool
    """
    return x % 2 == 0


def same_parity(x, *z):
    """
    :type x: int
    :type z: object
    :rtype: FunctionType
    """
    y = list(*z)

    def same_parity_iter(a):
        """
        :type a: FunctionType | object
        :return:
        """
        if is_null(a):
            return None
        else:
            b = car(a)  # type: int
            if is_even(x - b):
                return cons(b, same_parity_iter(cdr(a)))
            else:
                return same_parity_iter(cdr(a))

    return cons(x, same_parity_iter(y))


class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(is_same_list(same_parity(1, 2, 3, 4), list(1, 3)))

    def test_case_2(self):
        self.assertTrue(is_same_list(same_parity(2, 3, 4, 5, 6, 7),
                                     list(2, 4, 6)))


if __name__ == '__main__':
    unittest.main()
