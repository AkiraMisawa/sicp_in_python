# -*- coding: utf-8 -*-


def can_divide(a, b):
    return b % a == 0


def find_divisor(n, test_divisor):
    if test_divisor**2 > n:
        return n
    elif can_divide(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)


def smallest_devisor(n):
    return find_divisor(n, 2)


def main():
    result = [smallest_devisor(i) for i in [199, 1999, 19999]]
    print(result)


if __name__ == '__main__':
    main()
