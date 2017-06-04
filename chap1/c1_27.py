# -*- coding: utf-8 -*-
from c1_24 import expmod


def carmichael_test(n):
    '''
    nより小さいすべての正整数2対してa^n = a (mod n)を確認する
    Args:
        n (int): 正整数
    Returns:
        bool: すべて成功ならカーマイケル数はFermatテストを騙す
    '''
    def ctest(a, i):
        if a == n:
            return i
        elif expmod(a, n, n) == a:
            return ctest(a + 1, i + 1)
        else:
            return ctest(a + 1, i)

    if ctest(1, 0) == n - 1:
        print("{} is a carmichael number.".format(n))
    else:
        print("{} is NOT a carmichael number.".format(n))
    return
    

def main():
    carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601]
    for c in carmichael_numbers:
        carmichael_test(c)
    not_carmichael_number = 1110
    carmichael_test(not_carmichael_number)


if __name__ == '__main__':
    main()
