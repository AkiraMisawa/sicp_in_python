import unittest
import chap1.c1_03 as c1


class UnitTestOfAboveFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            13, c1.sum_of_squares_of_two_larger_numbers_from_three(3, 2, 1))

    def test_case_2(self):
        self.assertEqual(
            97, c1.sum_of_squares_of_two_larger_numbers_from_three(-2, 4, 9))

    def test_case_3(self):
        self.assertEqual(
            90, c1.sum_of_squares_of_two_larger_numbers_from_three(-10, -9, 3))


if __name__ == '__main__':
    unittest.main()
