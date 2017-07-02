import c2_7
import utility
import unittest


def sub_interval(x, y):
    lx = c2_7.lower_bound(x)
    ux = c2_7.upper_bound(x)
    ly = c2_7.lower_bound(y)
    uy = c2_7.upper_bound(y)
    return c2_7.make_interval(lx - uy, ux - ly)


class UnitTestOfIntervalArithmetic(unittest.TestCase):
    def setUp(self):
        self.interval0 = c2_7.make_interval(-3, 5)
        self.interval1 = c2_7.make_interval(2, 11)

    def test_sub_interval(self):
        result = sub_interval(self.interval0, self.interval1)
        self.assertEqual(-14, utility.car(result))
        self.assertEqual(3, utility.cdr(result))


if __name__ == '__main__':
    unittest.main()
