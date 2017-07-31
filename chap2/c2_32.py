from utility import car, cdr, cons, list, print_list, append, map, is_null, is_same_list


def subsets(l):
    if is_null(l):
        return list(list())
    rest = subsets(cdr(l))
    return append(rest, map(lambda x: cons(car(l), x) , rest))


if __name__ == '__main__':
    x = list(1, 2, 3)
    sub_x = subsets(x)
    print_list(x)
    print_list(sub_x)
