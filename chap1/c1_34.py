# -*- coding: utf-8 -*-


def f(g):
    return g(2)


def main():
    print(f(lambda x: x*x))
    print(f(lambda x: x*(x+1)))
    # print(f(f)) TypeError: 'int' object is not callable
    # f(g)の宣言でgに2を適用していることから、gの定義域はNumeric Type
    # g:Numeric->Tの形になる。従ってfは
    # f:Functor(Numeric->T)->T
    # の形になる
    # f自体はFunctor(Numeric->T)の形ではないので、
    # f(f)は呼び出せない


if __name__ == '__main__':
    main()
