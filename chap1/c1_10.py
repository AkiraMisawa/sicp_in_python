# -*- coding: utf-8 -*-
'''
アッカーマン関数を計算する
'''


def A(x, y):
    if y == 0:
        return 0
    if x == 0:
        return 2 * y
    if y == 1:
        return 2
    else:
        return A(x - 1, A(x, y - 1))


def f(n):
    '''
    f(n) := 2 * n
    '''
    return A(0, n)


def g(n):
    '''
    g(n) := 2^n
    '''
    return A(1, n)


def h(n):
    '''
    h(n) := 2^(2^(2^(2^(...))))
    2がどんどん(n層)べきべきになっていく
    '''
    return A(2, n)


def k(n):
    return 5 * n * n


def main():
    print("Hello my beautiful world!!")


if __name__ == '__main__':
    main()
