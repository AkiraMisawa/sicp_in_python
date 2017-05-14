# -*- coding: utf-8 -*-
"""
in jsicp p.38
"""
import math


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    def fib_iter(a, b, counter):
        if counter == 0:
            return b
        else:
            return fib_iter(a + b, a, counter - 1)

    return fib_iter(1, 0, n)


def calculate_golden_ratio():
    ret = 0.5 * (1 + math.sqrt(5))
    return ret


def main():
    result = [fib(i) for i in range(20)]
    result2 = [fib2(i) for i in range(20)]
    print(result)
    print(result2)
    
    n = 10
    fib_approx = math.pow(calculate_golden_ratio(), n) / math.sqrt(5)
    print("phi^{0} = {1}".format(n, fib_approx))
    print("fib({0}) = {1}".format(n, fib(n)))


if __name__ == '__main__':
    main()
