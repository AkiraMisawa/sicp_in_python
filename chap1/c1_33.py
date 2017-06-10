# -*- coding: utf-8 -*-
import operator
import c1_22 as c1


def accumulate(combiner, null_value, term, a, next, b):
    if a > b:
        return null_value
    else:
        return combiner(
            term(a),
            accumulate(combiner, null_value, term, next(a), next, b))

# def sum(term, a, next, b):
#     return accumulate(operator.add, 0, term, a, next, b)


# def prod(term, a, next, b):
#     return accumulate(operator.mul, 1, term, a, next, b)


def filtered_accumulate(predicate, combiner, null_value, term, a, next, b):
    if a > b:
        return null_value
    if predicate(a):
        return combiner(
            term(a),
            filtered_accumulate(predicate, combiner, null_value, term, next(a), next, b))
    else:
        return filtered_accumulate(predicate, combiner, null_value, term, next(a), next, b)


def prime_squared_sum(a, b):
    def square(x): return x**2

    def inc(n): return n + 1
    return filtered_accumulate(c1.is_prime, operator.add, 0, square, a, inc, b)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def coprime_product(n):
    return filtered_accumulate(
        lambda i: gcd(i, n) == 1,
        operator.mul,
        1,
        lambda x: x,
        1,
        lambda i: i + 1,
        n)


def main():
    print(prime_squared_sum(1, 10))
    print(coprime_product(10))
    print(c1.is_prime(1))
    # print(sum(
    #     lambda x: x,
    #     1,
    #     lambda i: i + 1,
    #     10))
    # print(prod(
    #     lambda x: x,
    #     1,
    #     lambda i: i + 1,
    #     10))


if __name__ == '__main__':
    main()
