def calc_exponent(n, base):
    if n % base == 0:
        return 1 + calc_exponent(n / base, base)
    else:
        return 0


def cons(a, b):
    return (2**a) * (3**b)


def car(r):
    return calc_exponent(r, 2)


def cdr(r):
    return calc_exponent(r, 3)


def main():
    r = cons(266, 4)
    print(car(r))
    print(cdr(r))


if __name__ == '__main__':
    main()
