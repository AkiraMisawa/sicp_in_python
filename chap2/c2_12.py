import utility


def make_center_width(c, w):
    return utility.make_interval(c - w, c + w)


def center(interval):
    l = utility.lower_bound(interval)
    u = utility.upper_bound(interval)
    return 0.5 * (l + u)


def width(interval):
    l = utility.lower_bound(interval)
    u = utility.upper_bound(interval)
    return 0.5 * (u - l)


def make_center_percent(c, p):
    """
    percent_error = width / center * 100
    """
    real_width = c * p / 100.0
    return make_center_width(c, real_width)


def percent(interval):
    c = center(interval)
    w = width(interval)
    percent = w / c * 100.0
    return percent


def main():
    interval0 = make_center_percent(1, 5)
    utility.print_interval(interval0)
    print(percent(interval0))


if __name__ == '__main__':
    main()
