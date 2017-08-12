# -*- coding: utf-8 -*-
from math import log


def tolerance():
    return 0.00001


def fixed_point(f, first_guess):
    def close_enough(v1, v2):
        return abs(v1-v2) < tolerance()

    def try_(guess):
        next_ = f(guess)
        print(next_)
        if close_enough(guess, next_):
            return next_
        else:
            return try_(next_)

    return try_(first_guess)


def main():
    # without ave damping, 33回
    fixed_point(lambda x: log(1000)/log(x), 10.0)
    # with ave damping, 10回
    fixed_point(lambda x: 1/2*(x+log(1000)/log(x)), 10.0)

    
if __name__ == '__main__':
    main()
