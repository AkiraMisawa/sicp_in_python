import unittest
import chap1.c1_30 as c1


class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1, c1.sumiter(c1.square, 1, c1.next, 1))

    def test_case_2(self):
        self.assertEqual(0, c1.sumiter(c1.square, 2, c1.next, 1))

    def test_case_3(self):
        self.assertEqual(385, c1.sumiter(c1.square, 1, c1.next, 10))


if __name__ == '__main__':
    unittest.main()
