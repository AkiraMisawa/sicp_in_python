import unittest

import chap1.utility as utility


class TestUtility(unittest.TestCase):
    def test_average(self):
        self.assertEqual(utility.average(1.0, 2.0), 1.5)
        self.assertEqual(utility.average(-5.0, -4.0), -4.5)

    def test_identity(self):
        self.assertEqual(utility.identity(1.0), 1.0)
        self.assertEqual(utility.identity(-1.0), -1.0)

    def test_square(self):
        self.assertEqual(utility.square(3.0), 9.0)
        self.assertEqual(utility.square(-2.0), 4.0)

    def test_cube(self):
        self.assertEqual(utility.cube(2.0), 8.0)
        self.assertEqual(utility.cube(-3.0), -27.0)

    def test_inc(self):
        self.assertEqual(utility.inc(1), 2)
        self.assertEqual(utility.inc(-8), -7)

    def test_dec(self):
        self.assertEqual(utility.dec(3), 2)
        self.assertEqual(utility.dec(-2), -3)

    def test_double(self):
        self.assertEqual(utility.double(2.0), 4.0)
        self.assertEqual(utility.double(-5), -10)

    def test_halve(self):
        self.assertEqual(utility.halve(10), 5)
        self.assertEqual(utility.halve(9), 4)
        self.assertEqual(utility.halve(-5), -3)

    def test_is_even(self):
        self.assertTrue(utility.is_even(2))
        self.assertTrue(not utility.is_even(3))
        self.assertTrue(utility.is_even(-2))
        self.assertTrue(not utility.is_even(-3))


if __name__ == '__main__':
    unittest.main()
