def compose(f,g):
    return lambda x:f(g(x))

def square(x):
    return x*x

def inc(x):
    return x+1

def main():
    print(compose(square,inc)(6))

if __name__ == '__main__':
    main()
