# -*- coding: utf-8 -*-
"""for utility functions"""


def cons(a, b):
    return lambda x: x(a, b)


def car(x):
    if x is None:
        return None
    else:
        return x(lambda a, b: a)


def cdr(x):
    if x is None:
        return None
    else:
        return x(lambda a, b: b)


# noinspection PyShadowingBuiltins
def list(*x):
    """
    :type x: object
    :rtype: FunctionType | None
    """
    def list_iter(*y, b):
        """
        :type y: object
        :type b: object
        :rtype: FunctionType | None
        """
        if len(y) == 0:
            return None
        elif len(y) == 1:
            a = y[0]
            return cons(a, b)
        else:
            a = y[-1]
            z = y[:-1]
            return list_iter(*z, b=cons(a, b))

    return list_iter(*x, b=None)


def is_null(items):
    """
    :type items: FunctionType | None
    :rtype: boll
    """
    return items is None


def length(items):
    """
    :type items: FunctionType | None
    :rtype: int
    """
    def length_iter(a, count):
        """
        :type a: FunctionType | None
        :type count: int
        :rtype: int
        """
        if is_null(a):
            return count
        else:
            return length_iter(cdr(a), count + 1)

    return length_iter(items, 0)


def list_ref(items, n):
    """
    :type items: FunctionType
    :type n: int
    :rtype: object
    """
    def list_ref_iter(x, count):
        """
        :type x: FunctionType
        :type count: int
        :rtype: FunctionType | object
        """
        if count == 0:
            return car(x)
        else:
            return list_ref_iter(cdr(x), count - 1)

    if is_null(items):
        raise ValueError('empty list')
    items_length = length(items)
    if n < 0:
        n += items_length
    if n >= items_length or n < 0:
        raise ValueError('list index out of range')
    return list_ref_iter(items, n)


def is_list(x):
    return callable(x)


def is_same_list(lst1, lst2):
    def is_same_element(x1, x2):
        if is_list(x1) == is_list(x2):
            if is_list(x1):
                return is_same_list(x1, x2)
            else:
                return x1 == x2
        else:
            return False

    if length(lst1) != length(lst2):
        return False
    elif length(lst1) == 0:
        return True
    else:
        is_same_car = is_same_element(car(lst1), car(lst2))
        is_same_cdr = is_same_list(cdr(lst1), cdr(lst2))
        return is_same_car and is_same_cdr


def append(list1, list2):
    """
    :type list1: FunctionType | None
    :type list2: FunctionType | None
    :rtype: FunctionType | None
    """
    if is_null(list1):
        return list2
    else:
        return cons(car(list1), append(cdr(list1), list2))


# noinspection PyShadowingBuiltins
def map(proc, items):
    """
    :type proc: FunctionType
    :type items: FunctionType | None
    :rtype: FunctionType | None
    """
    def map_to_element(proc, x):
        if is_list(x):
            return list(map(proc, x))
        else:
            return list(proc(x))

    if is_null(items):
        return None
    else:
        #print('tree: {0}'.format(list_to_str(tree)))
        lhs = map_to_element(proc, car(items))
        rhs = map(proc, cdr(items))
        return append(lhs, rhs)


def make_interval(a, b):
    return cons(a, b)


def lower_bound(interval):
    return car(interval)


def upper_bound(interval):
    return cdr(interval)


def print_interval(interval):
    print("[{0}, {1}]".format(lower_bound(interval), upper_bound(interval)))


def list_to_str(lst):
    def one_element_to_str(x):
        if is_list(x):
            return list_to_str(x) + ' '
        else:
            return str(x) + ' '

    def to_str_impl(lst):
        if not is_null(lst):
            return one_element_to_str(car(lst)) + to_str_impl(cdr(lst))
        else:
            return ''

    return '( ' + to_str_impl(lst) + ')'


def print_list(lst):
    print(list_to_str(lst))


def print_cons(lst):
    print('( ' + str(car(lst)) + ' ' + str(cdr(lst)) + ' )')


def accumulate(op, initial, sequence):
    if is_null(sequence):
        return initial
    else:
        return op(car(sequence),
                  accumulate(op, initial, cdr(sequence)))


def main():
    print("Hello my beautiful world!!")


if __name__ == '__main__':
    main()
