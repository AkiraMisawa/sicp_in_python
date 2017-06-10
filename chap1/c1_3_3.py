# coding=utf-8
"""1.3.3"""


def average(x, y):
    """
    :type x: float
    :type y: float
    :rtype: float
    """
    return (x + y) / 2


def is_close_enough(x, y, epsilon=1e-3):
    """
    :type x: float
    :type y: float
    :type epsilon: float
    :rtype: bool
    """
    return abs(x - y) < epsilon


def is_positive(x):
    """
    :type x: float
    :rtype: bool
    """
    return x > 0


def is_negative(x):
    """
    :type x: float
    :rtype: bool
    """
    return x < 0


def search(f, neg_point, pos_point):
    """
    :type f: float -> float
    :type neg_point: float
    :type pos_point: float
    :rtype: float
    """
    midpoint = average(neg_point, pos_point)
    if is_close_enough(neg_point, pos_point):
        return midpoint
    else:
        test_value = f(midpoint)
        if is_positive(test_value):
            return search(f, neg_point, midpoint)
        elif is_negative(test_value):
            return search(f, midpoint, pos_point)
        else:
            return midpoint


def half_interval_method(f, a, b):
    """
    :type f: float -> float
    :type a: float
    :type b: float
    :rtype: float
    """
    a_value = f(a)
    b_value = f(b)
    if is_negative(a_value) and is_positive(b_value):
        return search(f, a, b)
    elif is_negative(b_value) and is_positive(a_value):
        return search(f, b, a)
    else:
        raise ValueError('Values are not of opposite sign')


def fixed_point(f, first_guess, tolerance=1e-5):
    """
    :type f: float -> float
    :type first_guess: float
    :type tolerance: float
    :rtype: float
    """
    def try_next(guess):
        """
        :type guess: float
        :rtype: float
        """
        next_val = f(guess)
        if is_close_enough(guess, next_val, tolerance):
            return next_val
        else:
            return try_next(next_val)

    return try_next(first_guess)
