from utility import cons, car, cdr, list, is_null, is_same_list


def square(x):
    return x * x


def bad_square_list(items):
    def iter(things, answer):
        if is_null(things):
            return answer
        else:
            iter(cdr(things), cons(answer, square(car(things))))

    iter(items, None)


if __name__ == '__main__':
    L1 = list(1, 2, 3)
    print(bad_square_list(L1))  # None
