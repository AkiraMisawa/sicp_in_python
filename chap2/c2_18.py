import utility
import unittest


def reverse(l):
    if utility.is_null(l):
        return None
    elif utility.length(l) == 1:
        return l
    else:
        x = utility.car(l)
        xs = utility.cdr(l)
        return utility.append(reverse(xs), utility.list(x))


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case1(self):
        l = utility.list(1, 2, 3, 4)
        l_rev = reverse(l)
        l_rev_ans = utility.list(4, 3, 2, 1)
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))

    def test_case2(self):
        a = utility.list(1, 2)
        b = utility.list(3, 4)
        l = utility.list(a, b)
        l_rev = reverse(l)
        l_rev_ans = utility.list(b, a)
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))


if __name__ == '__main__':
    unittest.main()
