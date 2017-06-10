# -*- coding: utf-8 -*-
import random
import c1_23 as c1


def is_even(n):
    return n % 2 == 0


def expmod(base, exp, m):
    '''
    法mに関するbase^{exp}の剰余を返す
    Args:
        base (int): 底
        exp (int): べき指数
        m (int): 法
    Returns:
        int: 法mに関するbase^{exp}の剰余
    '''
    if exp == 0:
        return 1
    elif is_even(exp):
        return (expmod(base, exp / 2, m))**2 % m
    else:
        return (base * (expmod(base, exp - 1, m))) % m


def fermat_test(n):
    '''
    Fermatの小定理: 「n:素数, a(< n):正の整数 ==> a^n == n (mod a)」に基づき，nが素数であるかテストする
    Args:
        n (int): 正整数
    Returns:
        bool: nが素数である可能性
    '''
    def try_it(a):
        return expmod(a, n, n) == a
    return try_it(random.randint(1, n - 1))


def fast_prime(n, times):
    '''
    nに対してtimes回Fermatテストを行う
    Args:
        n (int): 正整数
        times (int): テスト回数
    Returns:
        bool: テストが全て成功すればTrue, そうでなければFalse.
    '''
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False


def generate_fast_prime_tester(times):
    '''
    Fermatテストを行う関数を返す
    Args:
        times (int): Fermatテストを行う回数
    Returns:
        function: times回Fermatテストを行う関数
    '''
    return lambda p: fast_prime(p, times)


def main():
    fermat_tester = generate_fast_prime_tester(10)
    primes0 = [1009, 1013, 1019]
    primes1 = [10007, 10009, 10037]
    primes2 = [100003, 100019, 100043]
    primes3 = [1000003, 1000033, 1000037]
    c1.show_prime_test(primes0, fermat_tester)
    c1.show_prime_test(primes1, fermat_tester)
    c1.show_prime_test(primes2, fermat_tester)
    c1.show_prime_test(primes3, fermat_tester)


if __name__ == '__main__':
    main()
