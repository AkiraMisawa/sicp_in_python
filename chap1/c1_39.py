import c1_37 as func


def tan_cf(x, k):
    def ni(i):
        if i == 1:
            return x
        else:
            return -x ** 2

    def di(i):
        return 2 * i - 1

    return x/(1+func.cont_frac_recur(ni, di, k))


def main():
    for r in range(1, 20):
        print(r, tan_cf(0.5, r))


if __name__ == '__main__':
    main()
