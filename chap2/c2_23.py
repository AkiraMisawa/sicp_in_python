import utility


def for_each(f, lst):
    if not utility.is_null(lst):
        f(utility.car(lst))
        for_each(f, utility.cdr(lst))


def main():
    for_each(print, utility.list(57, 321, 88))


if __name__ == '__main__':
    main()
