# -*- coding: utf-8 -*-
import time
import sys
sys.setrecursionlimit(1000000)


def next(n):
    return 3 if n == 2 else n + 2


def find_divisor(n, test_divisor):
    if test_divisor**2 > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n, next(test_divisor))


def smallest_divisor(n):
    return find_divisor(n, 2)


def generate_prime_tester_using_next():
    def is_prime(n):
        return n == smallest_divisor(n)
    return is_prime


def report_prime(elapsed_time):
    print(" *** {}".format(elapsed_time))
    return


def start_prime_test(n, start_time, prime_tester):
    if prime_tester(n):
        report_prime(time.time() - start_time)
    return


def timed_prime_test(n, prime_tester):
    print("\n{}".format(n), end='')
    start_prime_test(n, time.time(), prime_tester)
    #print("")
    return


def show_prime_test(prime_list, prime_tester):
    for p in prime_list:
        timed_prime_test(p, prime_tester)
    return


def main():
    tester_next_ver = generate_prime_tester_using_next()
    primes0 = [1009, 1013, 1019]
    primes1 = [10007, 10009, 10037]
    primes2 = [100003, 100019, 100043]
    primes3 = [1000003, 1000033, 1000037]
    primes = [primes0, primes1, primes2, primes3]

    for ps in primes:
        show_prime_test(ps, tester_next_ver)


if __name__ == '__main__':
    main()
