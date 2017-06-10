def compose(f, g, x):
    return f(g(x))


def inc(x):
    return x + 1


def square(x):
    return x * x


print("square(inc(6))=", compose(f=square, g=inc, x=6))
