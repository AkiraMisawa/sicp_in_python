#T_p,q^2(a,b)=T_(p^2+q^2),(q^2+2pq)(a,b)

def fib(n):
    return fib_iter(1,0,0,1,n)

def fib_iter(a,b,p,q,count):
    if count==0:
        return b
    elif count%2==0:
        return fib_iter(a,b,p*p+q*q,q*q+2*p*q,count/2)
    else:
        return fib_iter(b*q+a*q+a*p,b*p+a*q,p,q,count-1)

print(fib(50))
