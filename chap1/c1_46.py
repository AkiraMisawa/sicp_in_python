import math


EPS = 1e-12


def is_good_enough(guess, x, eps=EPS):
    if abs((guess - x) / x) < eps:
        return True
    else:
        return False


def iterative_improve(improve, is_good_enough, x):
    next_x = improve(x)
    if is_good_enough(next_x, x):
        return next_x
    else:
        return iterative_improve(improve, is_good_enough, next_x)


def sqrt(x):
    return iterative_improve(lambda y: (x/y+y)/2, is_good_enough, 1.0)


def fixed_point(f):
    return iterative_improve(f, is_good_enough, 1.0)
    

print("sqrt(2) ~", sqrt(2), "...")
print("fixed point of cosx ~", fixed_point(math.cos), "...")
