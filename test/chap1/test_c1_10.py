import unittest
import chap1.c1_10 as c1


class AckermanFunctionTest(unittest.TestCase):
    def test_A(self):
        self.assertEqual(1024, c1.A(1, 10))
        self.assertEqual(65536, c1.A(2, 4))
        self.assertEqual(65536, c1.A(3, 3))

    def test_f(self):
        self.assertEqual(2, c1.f(1))
        self.assertEqual(4, c1.f(2))
        self.assertEqual(6, c1.f(3))
        self.assertEqual(20, c1.f(10))

    def test_g(self):
        self.assertEqual(2, c1.g(1))
        self.assertEqual(4, c1.g(2))
        self.assertEqual(256, c1.g(8))
        self.assertEqual(1024, c1.g(10))

    def test_h(self):
        self.assertEqual(2, c1.h(1))
        self.assertEqual(4, c1.h(2))
        self.assertEqual(16, c1.h(3))
        self.assertEqual(65536, c1.h(4))


if __name__ == '__main__':
    unittest.main()
