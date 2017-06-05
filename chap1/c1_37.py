
def cont_frac_iter(n,d,k,index):
    if index>k:
        return 0
    else:
        return n(index)/(d(index)+cont_frac_iter(n,d,k,index+1))

def cont_frac(n,d,k):
    return cont_frac_iter(n,d,k,1)

def main():
    f = lambda x:x
    print(cont_frac(f,f,2))

if __name__ == '__main__':
    main()
