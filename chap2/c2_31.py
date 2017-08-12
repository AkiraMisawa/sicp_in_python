import utility
import unittest


def is_pair(lst):
    if utility.is_list(lst):
        car_lst = utility.car(lst)
        cdr_lst = utility.cdr(lst)
        if (not utility.is_list(car_lst)) and (not utility.is_list(cdr_lst)):
            return True
    return False


def tree_map(proc, tree):
    return utility.map(proc, tree)


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case1(self):
        tr = utility.list(1, utility.list(
            2, utility.list(3, 4), 5), utility.list(6, 7))
        ans = utility.list(1, utility.list(
            4, utility.list(9, 16), 25), utility.list(36, 49))
        trmap = tree_map(lambda x: x ** 2, tr)
        self.assertTrue(utility.is_same_list(trmap, ans))


if __name__ == '__main__':
    unittest.main()
