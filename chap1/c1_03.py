# -*- coding: utf-8 -*-
'''
標準のunittestを使ってみる
- unittest.TestCaseのサブクラスでテストを定義できる
- テストしたい振る舞いごとにメソッドを定義できる
- unittest.TestCaseのクラスでのテストメソッドは"test"で始まらなければならない
'''


def sum_of_squares_of_two_larger_numbers_from_three(a, b, c):
    lst = [a, b, c]
    two_largers = sorted(lst, reverse=True)
    ret = two_largers[0] ** 2 + two_largers[1] ** 2
    return ret


def main():
    print("Hello my beautiful world!!")
    print(sum_of_squares_of_two_larger_numbers_from_three(3, 2, 1))


if __name__ == '__main__':
    main()
