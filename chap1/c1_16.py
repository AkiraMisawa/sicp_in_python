# -*- coding: utf-8 -*-


def fast_expt2(b, n):
    def is_even(x): return x % 2 == 0

    def square(x): return x * x

    def fast_expt_iter(a, b, n):
        """
        a * b^n: const.
        """
        if n == 0:
            return a
        if is_even(n):
            return fast_expt_iter(a, square(b), n / 2)
        else:
            return fast_expt_iter(a * b, b, n - 1)

    return fast_expt_iter(1, b, n)


def main():
    print("Hello my beautiful world!!")


if __name__ == '__main__':
    main()
