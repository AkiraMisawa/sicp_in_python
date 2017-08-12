# -*- coding: utf-8 -*-
import time
import sys

sys.setrecursionlimit(1000000)


def find_divisor(n, test_divisor):
    if test_divisor**2 > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)


def smallest_divisor(n):
    return find_divisor(n, 2)


def is_prime(n):
    return n == smallest_divisor(n)


def report_prime(elapsed_time):
    print(" *** {}".format(elapsed_time))
    return


def start_prime_test(n, start_time):
    if is_prime(n):
        report_prime(time.time() - start_time)
    return


def timed_prime_test(n):
    print("\n{}".format(n), end='')
    start_prime_test(n, time.time())
    return


def search_for_primes(a, b):
    '''
    aからbの範囲の連続した奇数について素数判定を行う
    '''
    start = a + 1 if a % 2 == 0 else a
    print("-----{0} to {1}-----".format(a, b))
    for n in range(start, b + 1, 2):
        timed_prime_test(n)
    return


def main():
    search_for_primes(1000, 1020)
    search_for_primes(10000, 10050)
    search_for_primes(100000, 100050)
    search_for_primes(1000000, 1000050)


if __name__ == '__main__':
    main()
