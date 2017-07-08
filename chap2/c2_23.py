import utility


def for_each(f, l):
    if not utility.is_null(l):
        f(utility.car(l))
        for_each(f, utility.cdr(l))


def main():
    def f(x): return print(x)
    for_each(f, utility.list(57, 321, 88))


if __name__ == '__main__':
    main()
