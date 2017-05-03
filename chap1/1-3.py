import unittest


def sum_of_squares_of_two_larger_numbers_from_three(a, b, c):
    lst = [a, b, c]
    two_largers = sorted(lst, reverse=True)
    ret = two_largers[0] ** 2 + two_largers[1] ** 2
    return ret


class UnitTestOfAboveFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            13, sum_of_squares_of_two_larger_numbers_from_three(3, 2, 1))

    def test_case_2(self):
        self.assertEqual(
            97, sum_of_squares_of_two_larger_numbers_from_three(-2, 4, 9))

    def test_case_3(self):
        self.assertEqual(
            90, sum_of_squares_of_two_larger_numbers_from_three(-10, -9, 3))


if __name__ == '__main__':
    unittest.main()
