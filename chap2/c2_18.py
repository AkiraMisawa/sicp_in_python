import utility
import unittest


def reverse(lst):
    if utility.is_null(lst):
        return None
    elif utility.length(lst) == 1:
        return lst
    else:
        x = utility.car(lst)
        xs = utility.cdr(lst)
        return utility.append(reverse(xs), utility.list(x))


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case1(self):
        lst = utility.list(1, 2, 3, 4)
        l_rev = reverse(lst)
        l_rev_ans = utility.list(4, 3, 2, 1)
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))

    def test_case2(self):
        a = utility.list(1, 2)
        b = utility.list(3, 4)
        lst = utility.list(a, b)
        l_rev = reverse(lst)
        l_rev_ans = utility.list(b, a)
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))


if __name__ == '__main__':
    unittest.main()
