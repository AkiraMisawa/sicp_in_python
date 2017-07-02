"""
interval arithmetic
"""
import utility
import unittest


def make_interval(a, b):
    return utility.cons(a, b)


def lower_bound(interval):
    return utility.car(interval)


def upper_bound(interval):
    return utility.cdr(interval)


def add_interval(x, y):
    lx = lower_bound(x)
    ux = upper_bound(x)
    ly = lower_bound(y)
    uy = upper_bound(y)
    return make_interval(lx + ly, ux + uy)


def mul_interval(x, y):
    lx = lower_bound(x)
    ux = upper_bound(x)
    ly = lower_bound(y)
    uy = upper_bound(y)
    p = [lx * ly, lx * uy, ux * ly, ux * uy]
    return make_interval(min(p), max(p))


def div_interval(x, y):
    return mul_interval(
        x,
        make_interval(1.0 / upper_bound(y), 1.0 / lower_bound(y)))


class UnitTestOfIntervalArithmetic(unittest.TestCase):
    def test_construct(self):
        a = 1
        b = 11
        interval = make_interval(a, b)

    def setUp(self):
        self.interval0 = make_interval(-3, 5)
        self.interval1 = make_interval(2, 11)

    def test_lower_bound(self):
        self.assertEqual(-3, lower_bound(self.interval0))
        self.assertEqual(2, lower_bound(self.interval1))

    def test_upper_bound(self):
        self.assertEqual(5, upper_bound(self.interval0))
        self.assertEqual(11, upper_bound(self.interval1))

    def test_add_interval(self):
        result = add_interval(self.interval0, self.interval1)
        self.assertEqual(-1, utility.car(result))
        self.assertEqual(16, utility.cdr(result))

    def test_mul_interval(self):
        result = mul_interval(self.interval0, self.interval1)
        self.assertEqual(-33, utility.car(result))
        self.assertEqual(55, utility.cdr(result))

    def test_div_interval(self):
        result = div_interval(self.interval0, self.interval1)
        self.assertAlmostEqual(-3 * 0.5, utility.car(result), delta=1e-15)
        self.assertEqual(5.0 * 0.5, utility.cdr(result))


if __name__ == '__main__':
    unittest.main()
