import c1_37 as func

def de_frac_conti(i):
    if i % 3 != 2:
        return 1
    else:
        return (i + 1) * 2 / 3

def main():
    ni = lambda i:1
    for r in range(1,20):
        print(r,func.cont_frac_recur(ni,de_frac_conti,r))

if __name__ == '__main__':
    main()
