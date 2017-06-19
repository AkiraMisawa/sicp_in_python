import utility


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def make_rat(n, d):
    return utility.cons(n, d)


def numer(x):
    return utility.car(x)


def denom(x):
    return utility.cdr(x)


def add_rat(x, y):
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x),
                    denom(x) * denom(y))


def sub_rat(x, y):
    return make_rat(numer(x) * denom(y) - numer(y) * denom(x),
                    denom(x) * denom(y))


def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def div_rat(x, y):
    return make_rat(numer(x) * denom(y), denom(x) * numer(y))


def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def make_rat(n, d):
    if d < 0:
        return make_rat(-n, -d)
    g = gcd(n, d)
    return utility.cons(n // g, d // g)


def print_rat(x):
    print(numer(x), "/", denom(x))


def main():
    print_rat(make_rat(3, 243))
    print_rat(add_rat(make_rat(1, 3), make_rat(2, 3)))
    print_rat(sub_rat(make_rat(1, -2), make_rat(2, 3)))


if __name__ == '__main__':
    main()
