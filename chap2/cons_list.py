import utility


def lis(*xs):
    if len(xs) == 0:
        return utility.cons(None, None)
    elif len(xs) == 1:
        return utility.cons(xs[0], None)
    else:
        x = xs[0]
        ys = xs[1:]
        return utility.cons(x, lis(*ys))


def length(l):
    if utility.car(l) is None:
        return 0
    else:
        if utility.cdr(l) is None:
            return 1
        else:
            return 1 + length(utility.cdr(l))


def print_list(l):
    def print_impl(l):
        if length(l) > 0:
            print(utility.car(l), end=" ")
            if length(l) > 1:
                print_impl(utility.cdr(l))

    print('(', end=" ")
    print_impl(l)
    print(')')


def main():
    print_list(lis(1, 2, 3, 4, 5.5))
    print(utility.car(lis(1, 2, 3, 4, 5.5)))
    print_list(utility.cdr(lis(1, 2, 3, 4, 5.5)))

    print_list(lis())
    print_list(lis(3))
    print_list(lis(3, 5))


if __name__ == '__main__':
    main()
