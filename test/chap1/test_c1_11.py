import unittest
import chap1.c1_11 as c1


class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(c1.f(1), c1.g(1))

    def test_case_2(self):
        self.assertEqual(c1.f(10), c1.g(10))

    def test_case_3(self):
        self.assertEqual(c1.f(20), c1.g(20))


if __name__ == '__main__':
    unittest.main()
