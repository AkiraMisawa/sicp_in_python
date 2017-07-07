import utility
import unittest


def us_coins():
    return utility.list(50, 25, 10, 5, 1)


def uk_coins():
    return utility.list(100, 50, 20, 10, 5, 2, 1, 0.5)


def first_denomination(coin_values):
    return utility.car(coin_values)


def except_first_denomination(coin_values):
    return utility.cdr(coin_values)


def no_more(coin_values):
    return utility.length(coin_values) == 0


def cc(amount, coin_values):
    if amount == 0:
        return 1
    elif amount < 0 or no_more(coin_values):
        return 0
    else:
        return cc(amount, except_first_denomination(coin_values)) + \
            cc(amount - first_denomination(coin_values), coin_values)


class UnitTestOfAboveFunctions(unittest.TestCase):
    def test_case(self):
        self.assertEqual(cc(100, us_coins()), 292)


if __name__ == '__main__':
    unittest.main()
