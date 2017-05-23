def next(n):
    if n==2:
        return 3
    else:
        return n+2

def smallest_divisor_impl(n):
    return find_divisor_impl(n,2)

def find_divisor_impl(n,test_divisor):
    if test_divisor**2>n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor_impl(n,next(test_divisor))
