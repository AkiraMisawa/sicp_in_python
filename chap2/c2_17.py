import utility


def last_pair(lst):
    if utility.is_null(lst):
        raise ValueError('empty list')

    if utility.is_null(utility.cdr(lst)):
        return utility.car(lst)
    else:
        return last_pair(utility.cdr(lst))


def main():
    lst = utility.list(23, 72, 149, 34)
    last = last_pair(lst)
    print(last)
    assert 34 == last


if __name__ == '__main__':
    main()
