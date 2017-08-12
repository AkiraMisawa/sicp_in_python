import utility
import unittest


def count_leaves(t):
    return utility.accumulate(lambda x, y: x + y, 0,
                              utility.map(lambda x: 1, t))


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(count_leaves(utility.list()), 0)
        self.assertEqual(count_leaves(utility.list(1, 2, 3, 4, 5)), 5)
        # x = utility.cons(utility.list(1, 2), utility.list(3, 4))
        # y = utility.map(lambda x: 1, x)
        # utility.print_list(y)
        # print(count_leaves(x))


if __name__ == '__main__':
    unittest.main()
