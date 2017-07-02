# coding=utf-8
"""1.32"""
from utility import cube, inc, identity


def accumulate_recur(combiner, null_value, term, a, next_fun, b):
    """
    :type combiner: (float, float) -> float
    :type null_value: float
    :type term: int -> float
    :type a: int
    :type next_fun: int -> int
    :type b: int
    :rtype: float
    """
    if a > b:
        return null_value
    else:
        return combiner(
            term(a),
            accumulate_recur(combiner, null_value, term,
                             next_fun(a), next_fun, b)
        )


def accumulate_iter(combiner, null_value, term, a, next_fun, b):
    """
    :type combiner: (float, float) -> float
    :type null_value: float
    :type term: int -> float
    :type a: int
    :type next_fun: int -> int
    :type b: int
    :rtype: float
    """
    def iter_fun(x, result):
        """
        :type x: int
        :type result: float
        :rtype float
        """
        if x > b:
            return result
        else:
            return iter_fun(next_fun(x), combiner(term(x), result))

    return iter_fun(a, null_value)


def summation_recur(term, a, next_fun, b):
    """
    :type term: int -> float
    :type a: int
    :type next_fun: int -> int
    :type b: int
    :rtype: float
    """
    return accumulate_recur(lambda x, y: x + y, 0, term, a, next_fun, b)


def summation_iter(term, a, next_fun, b):
    """
    :type term: int -> float
    :type a: int
    :type next_fun: int -> int
    :type b: int
    :rtype: float
    """
    return accumulate_iter(lambda x, y: x + y, 0, term, a, next_fun, b)


def product_recur(term, a, next_fun, b):
    """
    :type term: int -> float
    :type a: int
    :type next_fun: int -> int
    :type b: int
    :rtype: float
    """
    return accumulate_recur(lambda x, y: x * y, 1, term, a, next_fun, b)


def product_iter(term, a, next_fun, b):
    """
    :type term: int -> float
    :type a: int
    :type next_fun: int -> int
    :type b: int
    :rtype: float
    """
    return accumulate_iter(lambda x,y: x * y, 1, term, a,next_fun,b)

def main():
    """main"""
    def summation_cubes_recur(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return summation_recur(cube, a, inc, b)

    def summation_cubes_iter(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return summation_iter(cube, a, inc, b)

    def factorial_recur(n):
        """
        :type n: int
        :rtype: int
        """
        return product_recur(identity, 1, inc, n)

    def factorial_iter(n):
        """
        :type n: int
        :rtype: int
        """
        return product_iter(identity, 1, inc, n)

    assert summation_cubes_recur(1, 10) == 3025
    assert summation_cubes_iter(1, 10) == 3025
    assert factorial_recur(5) == 120
    assert factorial_iter(5) == 120


if __name__ == '__main__':
    main()
