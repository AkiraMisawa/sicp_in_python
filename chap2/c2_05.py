# -*- coding: utf-8 -*-
"""
非負整数のペアを数値と数値演算だけから作れることを示す。
aとbのペアは2^a 3^bと表すことにする。(pairの実装はカプセル化)
対応するcons, car, cdrを作る。
"""


def cons_(a, b):
    """
    2^a 3^b represents a pair of a and b
    """
    return 2 ** a * 3 ** b


def car_(pair):
    if pair % 2 == 0:
        return 1 + car_(pair / 2)
    else:
        return 0


def cdr_(pair):
    if pair % 3 == 0:
        return 1 + cdr_(pair / 3)
    else:
        return 0


def main():
    pair = cons_(4, 13)
    assert car_(pair) == 4
    assert cdr_(pair) == 13


if __name__ == '__main__':
    main()
