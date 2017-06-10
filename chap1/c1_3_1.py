# coding=utf-8
"""1.3.1"""


def summation(term, a, next_fun, b):
    """
    :type term: int -> float
    :type a: int
    :type next_fun: int -> int
    :type b: int
    :rtype: float
    """
    if a > b:
        return 0
    else:
        return term(a) + summation(term, next_fun(a), next_fun, b)
