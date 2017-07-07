import utility


def make_rectangle(width, height):
    return utility.cons(width, height)


def width_rectangle(r):
    return utility.car(r)


def length_rectangle(r):
    return utility.cdr(r)


def perimeter_rectangle(r):
    return 2 * (width_rectangle(r) + length_rectangle(r))


def area_rectangle(r):
    return width_rectangle(r) * length_rectangle(r)


def main():
    r = make_rectangle(4, 8)
    print(perimeter_rectangle(r))
    print(area_rectangle(r))


if __name__ == '__main__':
    main()
