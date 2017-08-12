# -*- coding: utf-8 -*-


def sumiter(term, a, next, b):
    def iter(a, result):
        if a > b:
            return result
        else:
            return iter(next(a), result + term(a))
    return iter(a, 0)


def next(x):
    return x + 1


def square(x):
    return x * x


def main():
    print("Hello my beautiful world!!")


if __name__ == '__main__':
    main()
