# -*- coding: utf-8 -*-


def recursive_process(operator, init, term, a, follow, b):
    if a > b:
        return init
    else:
        return operator(
            term(a),
            recursive_process(operator, init, term, follow(a), follow, b))


def iterative_process(operator, state, term, a, follow, b):
    if a > b:
        return state
    else:
        return iterative_process(
            operator,
            operator(state, term(a)),
            term,
            follow(a),
            follow,
            b)


def prod(a, b):
    return a*b


def sum(a, b):
    return a+b


def inc(a):
    return a+1


def identity(a):
    return a


def product_recursive(init, func, a, b):
    return recursive_process(prod, init, func, a, inc, b)


def product_iterative(init, func, a, b):
    return iterative_process(prod, init, func, a, inc, b)


def factorial_recursive(n):
    return product_recursive(1, identity, 1, n)


def factorial_iterative(n):
    return product_iterative(1, identity, 1, n)


def pi_term(a):
    return (2*a)*(2*a)/((2*a-1)*(2*a+1))


def pi_recursive(n):
    return product_recursive(2, pi_term, 1, n)


def pi_iterative(n):
    return product_recursive(2, pi_term, 1, n)


def main():
    print(factorial_recursive(16))
    print(factorial_iterative(16))

    print(pi_recursive(100))
    print(pi_iterative(100))


if __name__ == '__main__':
    main()
