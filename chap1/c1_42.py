def compose(f, g, x):
    return f(g(x))


def inc(x):
    return x + 1


def square(x):
    return x * x


def main():
    print("square(inc(6))=", compose(f=square, g=inc, x=6))


if __name__ == '__main__':
    main()
