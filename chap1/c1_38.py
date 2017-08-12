import math


def n(i):
    return 1.0


def d(i):
    if i % 3 != 2:
        return 1.0
    else:
        a = i // 3
        return 2.0 * (a + 1.0)


def cont_frac(n, d, k):
    def rec(i):
        if i > k:
            return 0.0
        else:
            return n(i)/(d(i) + rec(i+1))
    return rec(1)


def main():
    k = 100
    print("k =", k)
    print("e =", 2.0 + cont_frac(n, d, k), "...")
    print("e - e(k) =", math.e - 2.0 - cont_frac(n, d, k))


if __name__ == '__main__':
    main()
