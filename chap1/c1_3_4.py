# coding=utf-8
"""1.3.4"""

from c1_3_3 import average, fixed_point


def average_damp(f):
    """
    :type f: float -> float
    :rtype: float -> float
    """
    return lambda x: average(x, f(x))


def deriv(g, dx=1e-5):
    """
    :type g: float -> float
    :type dx: float
    :rtype: float -> float
    """
    return lambda x: (g(x + dx) - g(x)) / dx


def newton_transform(g):
    """
    :type g: float -> float
    :rtype: float -> float
    """
    return lambda x: (x - (g(x) / deriv(g)(x)))


def newton_method(g, guess):
    """
    :type g: float -> float
    :type guess: float
    :rtype: float
    """
    return fixed_point(newton_transform(g), guess)


def fixed_point_of_transform(g, transform, guess):
    """
    :type g: float -> float
    :type transform: (float -> float) -> (float -> float)
    :type  guess: float
    :rtype : float
    """
    return fixed_point(transform(g), guess)
