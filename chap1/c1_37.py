
def cont_frac_recurproc(n,d,k,index):
    if index>k:
        return 0
    else:
        return n(index)/(d(index)+cont_frac_recurproc(n,d,k,index+1))

def cont_frac_recur(n,d,k):
    return cont_frac_recurproc(n,d,k,1)

def cont_frac_iterproc(n,d,index,frac):
    if index==0:
        return frac
    else:
        return cont_frac_iterproc(n,d,index-1,n(index)/(d(index)+frac))

def cont_frac_iter(n,d,k):
    return cont_frac_iterproc(n,d,k,0)

def main():
    f = lambda x:x
    print(cont_frac_recur(f,f,5))
    print(cont_frac_iter(f,f,5))

if __name__ == '__main__':
    main()
