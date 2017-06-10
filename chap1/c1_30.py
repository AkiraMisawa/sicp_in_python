import unittest


def sumiter(term, a, next, b):
    def iter(a, result):
        if a > b:
            return result
        else:
            return iter(next(a), result + term(a))
    return iter(a, 0)


def next(x):
    return x + 1


def square(x):
    return x * x


class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1, sumiter(square, 1, next, 1))

    def test_case_2(self):
        self.assertEqual(0, sumiter(square, 2, next, 1))

    def test_case_3(self):
        self.assertEqual(385, sumiter(square, 1, next, 10))


if __name__ == '__main__':
    unittest.main()
