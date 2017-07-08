import utility
import unittest


def deep_reverse(l):
    def deep_reverse_element(a):
        if callable(a):
            return utility.list(deep_reverse(a))
        else:
            return utility.list(a)

    def deep_reverse_of_length_one(l):
        return deep_reverse_element(utility.car(l))

    utility.print_list(l)
    if utility.is_null(l):
        return None
    elif utility.length(l) == 1:
        return deep_reverse_of_length_one(l)
    else:
        x = utility.car(l)
        xs = utility.cdr(l)
        x_rev = deep_reverse_element(x)
        xs_rev = deep_reverse(xs)
        return utility.append(xs_rev, x_rev)


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case1(self):
        l = utility.list(1, 2, 3, 4)
        l_rev = deep_reverse(l)
        l_rev_ans = utility.list(4, 3, 2, 1)
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))

    def test_case2(self):
        a = utility.list(1, 2)
        b = utility.list(3, 4)
        l = utility.list(a, b)
        ll = utility.list(utility.list(1, 2), utility.list(3, 4))
        self.assertTrue(utility.is_same_list(l, ll))

    def test_case3(self):
        a = utility.list(1, 2)
        b = utility.list(3, 4)
        l = utility.list(a, b)
        l_rev = deep_reverse(l)
        l_rev_ans = utility.list(utility.list(4, 3), utility.list(2, 1))
        utility.print_list(l_rev)
        ll = utility.list(utility.list(1, 2), utility.list(3, 4))
        self.assertTrue(utility.is_same_list(l, ll))
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))


if __name__ == '__main__':
    unittest.main()
