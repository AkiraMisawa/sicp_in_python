import utility


def make_point(x, y):
    """
    represents a point
    :param x: x-coordinate
    :param y: y-coordinate
    :return: 2-dim coordinate
    """
    return utility.cons(x, y)


def make_segment(start, end):
    """
    create a segment from start point and end point
    :param start: start point of a segment
    :param end: end point of a segment
    :return: segment
    """
    return utility.cons(start, end)


def start_segment(segment):
    """
    return start point of segment
    :param segment: segment
    :return: start point of segment
    """
    return utility.car(segment)


def end_segment(segment):
    """
    return end point of segment
    :param segment: segment
    :return: end point of segment
    """
    return utility.cdr(segment)


def mid_point(segment):
    """
    return mid-point of segment
    :param segment:
    :return: mid-point of segment
    """
    s = start_segment(segment)
    e = end_segment(segment)
    x = 0.5 * (x_point(s) + x_point(e))
    y = 0.5 * (y_point(s) + y_point(e))
    return make_point(x, y)


def x_point(p):
    """
    return x-coordinate
    :param p: 2-dim point
    :return: x-coordinate
    """
    return utility.car(p)


def y_point(p):
    """
    return y-coordinate
    :param p: 2-dim point
    :return: y-coodinate
    """
    return utility.cdr(p)


def print_point(p):
    """
    show point
    :param p: 2-dim coordinate
    :return: nothing
    """
    print("({0}, {1})".format(x_point(p), y_point(p)))


def main():
    p0 = make_point(1, 2)
    p1 = make_point(3, 6)
    s0 = make_segment(p0, p1)
    m0 = mid_point(s0)
    print_point(m0)

    s1 = make_segment(
        make_point(-2, 2),
        make_point(2, -2))
    m1 = mid_point(s1)
    print_point(m1)


if __name__ == '__main__':
    main()
