# -*- coding: utf-8 -*-


def double(f):
    """
    Args:
        f (function): 引数が1つの手続き
    Returns:
        function: fを2回適用する手続き
    """
    return lambda x: f(f(x))


def main():
    def inc(n): return n + 1
    print(double(inc)(5))  # 7

    result = double(double(double))(inc)(5)
    print(result)  # 21


if __name__ == '__main__':
    main()
