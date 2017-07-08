import utility


def last_pair(list):
    if utility.is_null(list):
        raise ValueError('empty list')

    if utility.is_null(utility.cdr(list)):
        return utility.car(list)
    else:
        return last_pair(utility.cdr(list))


def main():
    lst = utility.list(23, 72, 149, 34)
    last = last_pair(lst)
    print(last)
    assert 34 == last


if __name__ == '__main__':
    main()
