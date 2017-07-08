import utility as utility


def make_interval(a, b):
    return utility.cons(a, b)


def upper_bound(x):
    return utility.cdr(x)


def lower_bound(x):
    return utility.car(x)


def add_interval(x, y):
    return make_interval(lower_bound(x) + lower_bound(y),
                         upper_bound(x) + upper_bound(y))


def mul_interval(x, y):
    p1 = lower_bound(x)
    p2 = lower_bound(y)
    p3 = upper_bound(x)
    p4 = upper_bound(y)
    return make_interval(min([p1, p2, p3, p4]),
                         max([p1, p2, p3, p4]))


def div_interval_new(x, y):
    if lower_bound(y) * upper_bound(y) <= 0:
        return ValueError
    else:
        return mul_interval(x, make_interval(1.0 / upper_bound(y), 1.0 / lower_bound(y)))


def main():
    i1 = make_interval(2, 5)
    i2 = make_interval(4, 7)


if __name__ == '__main__':
    main()
