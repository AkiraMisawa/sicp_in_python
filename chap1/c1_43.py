import c1_42 as func

def repeated(f,n):
    if n==1:
        return f
    else:
        return func.compose(repeated(f,n-1),f)

def main():
    print(repeated(func.square,2)(5))

if __name__ == '__main__':
    main()
