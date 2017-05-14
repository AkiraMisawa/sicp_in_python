# -*- coding: utf-8 -*-
"""
jsicp p.40
"""

def count_change(amount):
    return cc(amount, 5)


def cc(amount, kinds_of_coins):
    '''
    次のディクショナリのコインを使って1ドルを両替するやり方を数える
    '''
    # 利用可能な硬貨の種類の数をキーとし，一つ目の種類のコインの額面を返すディクショナリ
    first_denomination = {
        "1": 1,
        "2": 5,
        "3": 10,
        "4": 25,
        "5": 50
    }
    if amount == 0:
        return 1
    if (amount < 0) or (kinds_of_coins == 0):
        return 0
    else:
        ret1 = cc(amount, kinds_of_coins - 1)
        ret2 = cc(amount - first_denomination[str(kinds_of_coins)], kinds_of_coins)
        return ret1 + ret2


def main():
    result = count_change(100)
    print(result)


if __name__ == '__main__':
    main()
