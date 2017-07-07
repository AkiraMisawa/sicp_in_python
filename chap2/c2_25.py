# (1 3 (5 7) 9)
# ((7))
# (1 (2 (3 (4 (5 (6 7))))))
from utility import car, cdr, list


def main():
    lst0 = list(1, 3, list(5, 7), 9)
    seven0 = car(
        cdr(
            car(
                cdr(
                    cdr(lst0)))))

    lst1 = list(list(7))
    seven1 = car(car(lst1))

    assert 7 == seven0
    assert 7 == seven1


if __name__ == '__main__':
    main()
