import unittest


def zero():
    return lambda f: lambda x: x


def one():
    return lambda f: lambda x: f(x)


def two():
    return lambda f: lambda x: f(f(x))


def three():
    return lambda f: lambda x: f(f(f(x)))


def add(a, b):
    return lambda f: lambda x: a(f)(b(f)(x))


def inc(n):
    return n + 1


def eval_church(church):
    return church(inc)(0)


class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1, eval_church(one()))

    def test_case_2(self):
        self.assertEqual(2, eval_church(two()))

    def test_case_3(self):
        self.assertEqual(3, eval_church(three()))

    def test_case_4(self):
        self.assertEqual(3, eval_church(add(one(), two())))

    def test_case_5(self):
        self.assertEqual(2, eval_church(add(one(), one())))


if __name__ == '__main__':
    unittest.main()
