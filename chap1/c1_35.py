from math import cos

def tolerance():
    return 0.00001

def fixed_point(f,first_guess):
    def close_enough(v1,v2):
        return abs(v1-v2)<tolerance()

    def try_(guess):
        next_=f(guess)
        if close_enough(guess,next_):
            return next_
        else:
            return try_(next_)

    return try_(first_guess)

def main():
    #print(fixed_point(cos,1.0))
    print(fixed_point(lambda x:1+1/x,1.0))

if __name__ == '__main__':
    main()
