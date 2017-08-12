# -*- coding: utf-8 -*-
import random
import time


def fast_expt(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_expt(b, n / 2)**2
    else:
        return b * fast_expt(b, n - 1)


def expmod(base, exp, m):
    # これだとfast_expt(base, exp)の結果が大きくなりすぎる
    return fast_expt(base, exp) % m


def fermat_test(n):
    def try_it(a):
        return expmod(a, n, n) == a
    return try_it(random.randint(1, n - 1))


def fast_prime(n, times):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False


def generate_prime_teste(times):
    return lambda p: fast_prime(p, times)


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
    return


def show_prime_test(prime_list, prime_tester):
    for p in prime_list:
        timed_prime_test(p, prime_tester)
    return


def main():
    primes0 = [1009, 1013, 1019]
    primes1 = [10007, 10009, 10037]
    primes2 = [100003, 100019, 100043]
    primes3 = [1000003, 1000033, 1000037]

    prime_tester = generate_prime_teste(10)
    show_prime_test(primes0, prime_tester)
    show_prime_test(primes1, prime_tester)
    show_prime_test(primes2, prime_tester)
    show_prime_test(primes3, prime_tester)


if __name__ == '__main__':
    main()
