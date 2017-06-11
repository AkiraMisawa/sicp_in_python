# -*- coding: utf-8 -*-
from utility import average
from c1_16 import fast_expt2


def compose(f, g):
    return lambda x: f(g(x))


def repeate(f, n):
     if n == 0:
        return lambda x: x
     else:
         return compose(f, repeate(f, n - 1))


def average_damp(f):
    return lambda x: average(x, f(x))


def tolerance(): return 1e-8


def fixed_point(f, first_guess):
    def is_close_enough(v1, v2):
        return abs(v1 - v2) < tolerance()

    def try_(guess):
        next_ = f(guess)
        return next_ if is_close_enough(guess, next_) else try_(next)

    return try_(first_guess)


def find_n_th_root(n, x, num_of_smoothing):
    num_of_smoothing_avg_damp = repeate(average_damp, num_of_smoothing)
    proc = lambda y : x / (fast_expt2(y, n - 1))
    return fixed_point(num_of_smoothing_avg_damp(proc), 1.0)
    

def main():
    print(find_n_th_root(2, 2, 1))
    


if __name__ == '__main__':
    main()
