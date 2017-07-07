import utility


def make_segment(p, q):
    return utility.cons(p, q)


def start_segment(s):
    return utility.car(s)


def end_segment(s):
    return utility.cdr(s)


def make_point(x, y):
    return utility.cons(x, y)


def x_point(p):
    return utility.car(p)


def y_point(p):
    return utility.cdr(p)


def print_point(p):
    print("(", x_point(p), ",", y_point(p), ")")


def mid_point(p, q):
    return make_point((x_point(p) + x_point(q)) / 2.0,
                      (y_point(p) + y_point(q)) / 2.0)


def main():
    print_point(mid_point(make_point(2, 5), make_point(3, 9)))
    print_point(mid_point(make_point(-4.2, 5.5), make_point(35.3, 9.3)))
    print_point(start_segment(make_segment(make_point(-4.2, 5.5),
                                           make_point(35.3, 9.3))))
    print_point(end_segment(make_segment(make_point(-4.2, 5.5),
                                         make_point(35.3, 9.3))))


if __name__ == '__main__':
    main()
