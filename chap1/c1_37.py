# -*- coding: utf-8 -*-


def cont_frac_recur(n, d, k):
    """
    k項有限連分数
    Args:
        n (function): index(int)を受け取りintを返すt
        d (function): index(int)を受け取りintを返す
        k (int): 打ち切る項数
    Returns:
        float: k項有限連分数
    """
    def cont_frac_inner(index):
        if index > k:
            return 0
        else:
            return n(index) / (d(index) + cont_frac_inner(index + 1))

    return cont_frac_inner(1)


def cont_frac_iter(n, d, k):
    def cont_frac_iter_inner(residual, index):
        if index == 0:
            return residual
        else:
            res = n(index) / (d(index) + residual)
            return cont_frac_iter_inner(res, index - 1)

    return cont_frac_iter_inner(n(k) / d(k), k - 1)


def main():
    print("recurcive")
    for i in range(1, 20):
        print("k = {0}:  f = {1}"
              .format(i, cont_frac_recur(lambda x: 1.0, lambda x: 1.0, i)))

    print("iterative")
    for i in range(1, 20):
        print("k = {0}:  f = {1}"
              .format(i, cont_frac_iter(lambda x: 1.0, lambda x: 1.0, i)))

    # 1/phi=0.61803...なので11回で小数点第4位まで近似できる


if __name__ == '__main__':
    main()
