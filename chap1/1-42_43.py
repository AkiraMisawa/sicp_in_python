def compose(f,g):
    return lambda x:f(g(x))

def square(x):
    return x*x

def inc(x):
    return x+1

def repeated(f,n):
    if n==1:
        return f
    else:
        return compose(repeated(f,n-1),f)

print(compose(square,inc)(6))
print(repeated(square,2)(5))
