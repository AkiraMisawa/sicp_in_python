import utility
import c2_02 as plane


def make_rectangle(p, q):
    return utility.cons(p, q)


def start_rectangle(r):
    return utility.car(r)


def end_rectangle(r):
    return utility.cdr(r)


def width_rectangle(r):
    return abs(plane.x_point(start_rectangle(r))
               - plane.x_point(end_rectangle(r)))


def length_rectangle(r):
    return abs(plane.y_point(start_rectangle(r))
               - plane.y_point(end_rectangle(r)))


def perimeter_rectangle(r):
    return 2 * (width_rectangle(r) + length_rectangle(r))


def area_rectangle(r):
    return width_rectangle(r) * length_rectangle(r)


def main():
    p = plane.make_point(2, 6)
    q = plane.make_point(3, 9)
    r = make_rectangle(p, q)
    print(perimeter_rectangle(r))
    print(area_rectangle(r))


if __name__ == '__main__':
    main()
