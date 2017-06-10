# -*- coding: utf-8 -*-
import random


def expmod(base, exp, m):
    def is_even(x): return x % 2 == 0
    
    if exp == 0:
        return 1
    elif is_even(exp):
        rem = (expmod(base, exp / 2, m))**2 % m
        if rem > 1 and rem < m and rem**2 % m == 1:
            return 0
    else:
        return (base * (expmod(base, exp - 1, m))) % m


def miller_rabin_test(n):
    '''
    Fermatの小定理の変種: 「n:素数, a(< n):正の整数 ==> a^{n-1} == 1 (mod n)」 を用いたテスト
    Args:
        n (int): 正整数
    Returns:
        bool: nが素数ならTrue，そうでなければFalse
    '''
    def try_it(a):
        return expmod(a, n - 1, n) == 1

    result = try_it(random.randint(1, n - 1))
    if result:
        print("{} is a prime number.".format(n))
        return
    else:
        print("{} is NOT a prime number.".format(n))
        return
    

def main():
    carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601]
    for c in carmichael_numbers:
        miller_rabin_test(c)


if __name__ == '__main__':
    main()
