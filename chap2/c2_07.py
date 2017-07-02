"""
interval arithmetic
"""
import utility
import unittest


def add_interval(x, y):
    lx = utility.lower_bound(x)
    ux = utility.upper_bound(x)
    ly = utility.lower_bound(y)
    uy = utility.upper_bound(y)
    return utility.make_interval(lx + ly, ux + uy)


def mul_interval(x, y):
    lx = utility.lower_bound(x)
    ux = utility.upper_bound(x)
    ly = utility.lower_bound(y)
    uy = utility.upper_bound(y)
    p = [lx * ly, lx * uy, ux * ly, ux * uy]
    return utility.make_interval(min(p), max(p))


def div_interval(x, y):
    return mul_interval(
        x,
        utility.make_interval(
            1.0 / utility.upper_bound(y),
            1.0 / utility.lower_bound(y)))


class UnitTestOfIntervalArithmetic(unittest.TestCase):
    def test_construct(self):
        a = 1
        b = 11
        interval = utility.make_interval(a, b)

    def setUp(self):
        self.interval0 = utility.make_interval(-3, 5)
        self.interval1 = utility.make_interval(2, 11)

    def test_lower_bound(self):
        self.assertEqual(-3, utility.lower_bound(self.interval0))
        self.assertEqual(2, utility.lower_bound(self.interval1))

    def test_upper_bound(self):
        self.assertEqual(5, utility.upper_bound(self.interval0))
        self.assertEqual(11, utility.upper_bound(self.interval1))

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
