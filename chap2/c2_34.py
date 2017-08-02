import unittest
from utility import cons, car, cdr, list, print_list, is_null, map


def accumulate(op, initial, list):
    if is_null(list):
        return initial
    else:
        return op(car(list), accumulate(op, initial, cdr(list)))


def horner_eval(x, list):
    return accumulate(lambda this_coeff, higher_terms: this_coeff + higher_terms * x, 0, list)


class UnitTest(unittest.TestCase):
    def test_case_1(self):
        l = list(1, 0, 0)
        x = 2
        a = 1
        self.assertEqual(a, horner_eval(x, l))


    def test_case_2(self):
        l = list(1, 1, 1)
        x = 2
        a = 7
        self.assertEqual(a, horner_eval(x, l))


    def test_case_3(self):
        l = list(1, 3, 0, 5, 0, 1)
        x = 2
        a = 79
        self.assertEqual(a, horner_eval(x, l))


if __name__ == '__main__':
    unittest.main()
