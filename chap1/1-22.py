import time

def smallest_divisor(n):
    return find_divisor(n,2)

def find_divisor(n,test_divisor):
    if test_divisor**2>n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n,test_divisor+1)

def prime(n):
    return n==smallest_divisor(n)

def timed_prime_test(n):
    print("")
    print(n,end='')
    start_prime_test(n,time.time())

def start_prime_test(n,start_time):
    if prime(n):
        report_prime(time.time()-start_time)

def report_prime(elapsed_time):
    print(" *** ",end='')
    print(elapsed_time,end='')

def search_for_primes(a,b):
    for n in range(a,b):
        if n%2!=0:
            timed_prime_test(n)
    print("")

search_for_primes(1000,1020)
search_for_primes(10000,10050)
search_for_primes(100000,100050)
#search_for_primes(1000000,1000050)
