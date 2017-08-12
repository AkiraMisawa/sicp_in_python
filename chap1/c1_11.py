def f(n):
    if n <= 2:
        return n
    else:
        return f(n-1) + 2*f(n-2) + 3*f(n-3)


def g(n):
    if n <= 2:
        return n
    else:
        return g_iter(2, 1, 0, 3, n)


def g_iter(f1, f2, f3, cnt, n):
    if cnt <= n:
        f1, f2, f3 = f1 + 2*f2 + 3*f3, f1, f2
        cnt += 1
        return g_iter(f1, f2, f3, cnt, n)
    else:
        return f1


def main():
    print("Hello my beautiful world!!")


if __name__ == '__main__':
    main()
