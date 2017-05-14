# -*- coding: utf-8 -*-
"""
in jsicp p.33
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n):
    # クロージャを定義することによりスコープが限定されて嬉しい
    def fact_iter(product, counter):
        if counter > n:
            return product
        else:
            return fact_iter(counter * product, counter + 1)

    return fact_iter(1, 1)


def main():
    result1 = [factorial(i) for i in range(10)]
    result2 = [factorial2(i) for i in range(10)]
    print(result1)
    print(result2)


if __name__ == '__main__':
    main()
