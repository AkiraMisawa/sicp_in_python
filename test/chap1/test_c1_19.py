import unittest
import chap1.c1_19 as c1


class FibLogScaleTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(0, c1.fib(0))

    def test_case2(self):
        self.assertEqual(1, c1.fib(2))

    def test_case3(self):
        self.assertEqual(8, c1.fib(6))

    def test_case4(self):
        self.assertEqual(55, c1.fib(10))

    def test_case5(self):
        self.assertEqual(4181, c1.fib(19))


if __name__ == '__main__':
    unittest.main()
