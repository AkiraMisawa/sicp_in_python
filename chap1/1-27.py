def test_congruent(n):
    for a in range(1,n):
        print_congruent(a,n)


def print_congruent(a,n):
    print(a,"^",n,"-",a,"=",congruent(a,n),"mod",n)

def congruent(a,n):
    return (a**n-a)%n

test_congruent(561)
