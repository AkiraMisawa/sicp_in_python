# (1 3 (5 7) 9)
# ((7))
# (1 (2 (3 (4 (5 (6 7))))))
from utility import car, cdr, list, print_list


def main():
    lst0 = list(1, 3, list(5, 7), 9)
    print_list(lst0)
    seven0 = car(
        cdr(
            car(
                cdr(
                    cdr(lst0)))))

    lst1 = list(list(7))
    print_list(lst1)
    seven1 = car(car(lst1))

    lst2 = list(1, list(2, list(3, list(4, list(5, list(6, 7))))))
    print_list(lst2)
    seven2 = car(cdr(
            car(cdr(
                car(cdr(
                    car(cdr(
                        car(cdr(
                            car(cdr(lst2))))))))))))

    assert 7 == seven0
    assert 7 == seven1
    assert 7 == seven2


if __name__ == '__main__':
    main()
