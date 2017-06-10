# -*- coding: utf-8 -*-
import math
import sys
sys.setrecursionlimit(10000)


def generate_sum(term_op, a, next_op, b):
    '''
    \sum^b_{n = a} f(n) = f(a) + ... + f(b)
    term_op: 手続き
    next_op: 手続き
    '''
    def sum(a, b):
        if a > b:
            return 0
        else:
            return term_op(a) + sum(next_op(a), b)
    return sum


def calculate_h(a, b, n):
    return float(b - a) / float(n)


def simpson_rule(f, a, b, n):
    h = calculate_h(a, b, n)

    def simpson_term(x):
        return f(x) + 4.0 * f(x + h) + f(x + 2.0 * h)

    def simpson_next(x):
        return x + 2.0 * h

    sum = generate_sum(simpson_term, a, simpson_next, b - h)
    return sum(a, b) * h / 3.0


def simple_integral(f, a, b, dx):
    def add_dx(x): return x + dx
    sum = generate_sum(f, a + 0.5 * dx, add_dx, b)
    return dx * sum(a, b)


def calculate_relative_error(expect, actual):
    return abs(expect - actual) / expect if expect != 0.0 else math.nan
    

def main():
    def cube(x): return x * x * x

    simpson_result100 = simpson_rule(cube, 0.0, 1.0, 100)
    simpson_result1000 = simpson_rule(cube, 0.0, 1.0, 1000)
    simple_result100 = simple_integral(cube, 0.0, 1.0, 0.01)
    simple_result1000 = simple_integral(cube, 0.0, 1.0, 0.001)

    expect = 0.25
    print(calculate_relative_error(expect, simpson_result100))
    print(calculate_relative_error(expect, simpson_result1000))
    print(calculate_relative_error(expect, simple_result100))
    print(calculate_relative_error(expect, simple_result1000))


if __name__ == '__main__':
    main()
