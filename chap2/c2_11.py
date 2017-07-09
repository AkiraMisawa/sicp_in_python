import utility
import c2_07 as interval


def isGreaterThanZero(x):
    return interval.lower_bound(x) > 0


def isLessThanZero(x):
    return interval.upper_bound(x) < 0


def isSandwitchZero(x):
    return (not isLessThanZero(x)) and (not isGreaterThanZero(x))


def mul_interval(x, y):
    x0 = interval.lower_bound(x)
    y0 = interval.lower_bound(y)
    x1 = interval.upper_bound(x)
    y1 = interval.upper_bound(y)

    if isGreaterThanZero(x) and isGreaterThanZero(y):
        return interval.make_interval(x0 * y0, x1 * y1)
    elif isSandwitchZero(x) and isGreaterThanZero(y):
        return interval.make_interval(x0 * y1, x1 * y1)
    elif isLessThanZero(x) and isGreaterThanZero(y):
        return interval.make_interval(x0 * y1, x1 * y0)
    elif isGreaterThanZero(x) and isSandwitchZero(y):
        return mul_interval(y, x)
    elif isSandwitchZero(x) and isSandwitchZero(y):
        return interval.make_interval(min(x0 * y1, x1 * y0),
                                      max(x0 * y0, x1 * y1))
    elif isLessThanZero(x) and isSandwitchZero(y):
        return interval.make_interval(x0 * y1, x0 * y0)
    elif isGreaterThanZero(x) and isLessThanZero(y):
        return mul_interval(y, x)
    elif isSandwitchZero(x) and isLessThanZero(y):
        return mul_interval(y, x)
    elif isLessThanZero(x) and isLessThanZero(y):
        return interval.make_interval(x1 * y1, x0 * y0)


def main():
    i1 = interval.make_interval(1, 3)
    i2 = interval.make_interval(-3, 5)
    i3 = interval.make_interval(-4, -2)
    j1 = interval.make_interval(3, 4)
    j2 = interval.make_interval(-3, 0)
    j3 = interval.make_interval(-6, -1)
    utility.print_cons(mul_interval(i1, j1))
    utility.print_cons(mul_interval(i2, j1))
    utility.print_cons(mul_interval(i3, j1))
    utility.print_cons(mul_interval(i1, j2))
    utility.print_cons(mul_interval(i2, j2))
    utility.print_cons(mul_interval(i3, j2))
    utility.print_cons(mul_interval(i1, j3))
    utility.print_cons(mul_interval(i2, j3))
    utility.print_cons(mul_interval(i3, j3))


if __name__ == '__main__':
    main()
