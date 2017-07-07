# -*- coding: utf-8 -*-
import utility


def square(x):
    return x ** 2


def square_list(list):
    if utility.is_null(list):
        return utility.list()
    else:
        return utility.cons(
            square(utility.car(list)),
            square_list(utility.cdr(list)))


def square_list_with_map(list):
    return utility.map(lambda x: x ** 2, list)


def main():
    lst = utility.list(1, 2, 3, 4, 5)
    print(lst)
    result = square_list_with_map(lst)
    print(result)


if __name__ == '__main__':
    main()
