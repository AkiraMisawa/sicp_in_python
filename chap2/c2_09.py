import c2_7
import c2_08


def width(interval):
    l = c2_7.lower_bound(interval)
    u = c2_7.upper_bound(interval)
    return 0.5 * (u - l)


def main():
    interval0 = c2_7.make_interval(1, 3)
    interval1 = c2_7.make_interval(8, 10)
    interval2 = c2_7.make_interval(19, 21)

    added_intervals = [
        c2_7.add_interval(interval0, interval1),
        c2_7.add_interval(interval0, interval2),
        c2_7.add_interval(interval1, interval2)
    ]
    sub_intervals = [
        c2_08.sub_interval(interval0, interval1),
        c2_08.sub_interval(interval0, interval2),
        c2_08.sub_interval(interval1, interval2)
    ]
    added_widths = [width(itvl) for itvl in added_intervals]
    sub_widths = [width(itvl) for itvl in sub_intervals]
    print(added_widths)
    print(sub_widths)

    multiplied_intervals = [
        c2_7.mul_interval(interval0, interval1),
        c2_7.mul_interval(interval0, interval2),
        c2_7.mul_interval(interval1, interval2)
    ]
    multiplied_widths = [width(itvl) for itvl in multiplied_intervals]
    print(multiplied_widths)

    divided_intervals = [
        c2_7.div_interval(interval0, interval1),
        c2_7.div_interval(interval0, interval2),
        c2_7.div_interval(interval1, interval2)
    ]
    divided_widths = [width(itvl) for itvl in divided_intervals]
    print(divided_widths)


if __name__ == '__main__':
    main()
