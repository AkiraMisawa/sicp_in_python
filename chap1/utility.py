# coding=utf-8
"""
For utility functions.
"""

def average(x, y):
    """
    :type x: float
    :type y: float
    :rtype: float
    """
    return 0.5 * (x + y)


def identity(x):
    """
    :type x: float
    :rtype: float
    """
    return x


def square(x):
    """
    :type x: float
    :rtype: float
    """
    return x * x


def cube(x):
    """
    :type x: float
    :rtype: float
    """
    return x * x * x


def inc(x):
    """
    :type x: float
    :rtype: float
    """
    return x + 1


def dec(x):
    """
    :type x: float
    :rtype: float
    """
    return x - 1


def double(x):
    """
    :type x: float
    :rtype: float
    """
    return 2 * x


def halve(x):
    """
    :type x: int
    :rtype: int
    """
    return x // 2


def is_even(x):
    """
    :type x: int
    :rtype: bool
    """
    return x % 2 == 0
