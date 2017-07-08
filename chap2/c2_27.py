import utility
import unittest


def deep_reverse(lst):
    def deep_reverse_element(a):
        if callable(a):
            return utility.list(deep_reverse(a))
        else:
            return utility.list(a)

    def deep_reverse_of_length_one(lst):
        return deep_reverse_element(utility.car(lst))

    # utility.print_list(lst)
    if utility.is_null(lst):
        return None
    elif utility.length(lst) == 1:
        return deep_reverse_of_length_one(lst)
    else:
        x = utility.car(lst)
        xs = utility.cdr(lst)
        x_rev = deep_reverse_element(x)
        xs_rev = deep_reverse(xs)
        return utility.append(xs_rev, x_rev)


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case1(self):
        lst = utility.list(1, 2, 3, 4)
        l_rev = deep_reverse(lst)
        l_rev_ans = utility.list(4, 3, 2, 1)
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))

    def test_case2(self):
        a = utility.list(1, 2)
        b = utility.list(3, 4)
        lst = utility.list(a, b)
        ll = utility.list(utility.list(1, 2), utility.list(3, 4))
        self.assertTrue(utility.is_same_list(lst, ll))

    def test_case3(self):
        a = utility.list(1, 2)
        b = utility.list(3, 4)
        lst = utility.list(a, b)
        l_rev = deep_reverse(lst)
        l_rev_ans = utility.list(utility.list(4, 3), utility.list(2, 1))
        self.assertTrue(utility.is_same_list(l_rev, l_rev_ans))


if __name__ == '__main__':
    unittest.main()
