import unittest
import chap2.utility as utility


class TestUtility(unittest.TestCase):
    def test_cons(self):
        a = 1
        b = 2
        utility.cons(a, b)

    def test_car(self):
        a = 1
        b = 2
        x = utility.cons(a, b)
        self.assertEqual(a, utility.car(x))

    def test_cdr(self):
        a = 1
        b = 2
        x = utility.cons(a, b)
        self.assertEqual(b, utility.cdr(x))

    def test_empty_list(self):
        x = utility.list()
        self.assertEqual(None, utility.car(x))
        self.assertEqual(None, utility.cdr(x))

    def test_list_with_1_element(self):
        a = 1
        x = utility.list(a)
        self.assertEqual(a, utility.car(x))
        self.assertEqual(None, utility.cdr(x))

    def test_list_with_3_elements(self):
        a = 1
        b = 2
        c = 3
        x = utility.list(a, b, c)
        self.assertEqual(a, utility.car(x))
        self.assertEqual(b, utility.car(utility.cdr(x)))
        self.assertEqual(c, utility.car(utility.cdr(utility.cdr(x))))

    def test_list_length(self):
        x = utility.list()
        y = utility.list(1, 2, 3, 4, 5)
        self.assertEqual(0, utility.length(x))
        self.assertEqual(5, utility.length(y))

    def test_list_ref(self):
        a = 1
        b = 2
        c = 3
        x = utility.list(a, b, c)
        self.assertEqual(a, utility.list_ref(x, 0))
        self.assertEqual(b, utility.list_ref(x, 1))
        self.assertEqual(c, utility.list_ref(x, -1))

    def test_is_same_list(self):
        list1 = utility.list(1, 2, 3)
        list2 = utility.list(1, 2, 3)
        list12 = utility.list(list1, list2)
        list21 = utility.list(list2, list1)
        list3 = utility.list(utility.list(1, 2, 3), utility.list(1, 2, 3))
        self.assertTrue(utility.is_same_list(list1, list2))
        self.assertTrue(utility.is_same_list(list12, list21))
        self.assertTrue(utility.is_same_list(list12, list3))

    def test_my_map(self):
        x = utility.list(1, 2, 3)
        y = utility.list(2, 4, 6)
        self.assertTrue(
            utility.is_same_list(
                utility.map(lambda i: 2 * i, x),
                y))

    def test_case_9(self):
        a = utility.list()
        b = utility.list(1)
        c = utility.list(1, 2)
        d = utility.list(3, 4)
        e = utility.list(1, 2, d)
        f = utility.list(7, e, d)
        self.assertEqual(utility.list_to_str(a), '( )')
        self.assertEqual(utility.list_to_str(b), '( 1 )')
        self.assertEqual(utility.list_to_str(utility.list(b)), '( ( 1 ) )')
        self.assertEqual(utility.list_to_str(c), '( 1 2 )')
        self.assertEqual(utility.list_to_str(e), '( 1 2 ( 3 4 ) )')
        self.assertEqual(
            utility.list_to_str(f),
            '( 7 ( 1 2 ( 3 4 ) ) ( 3 4 ) )')

    def test_case10(self):
        self.assertEqual(
            utility.accumulate(lambda x, y: x + y, 0, utility.list(1, 2, 3)),
            6)
        self.assertEqual(
            utility.accumulate(lambda x, y: x * y, 1, utility.list(1, 2, 3)),
            6)
        accumulate_cons = utility.accumulate(
            lambda x, y: utility.cons(x, y),
            None,
            utility.list(1, 2, 3, 4, 5))
        self.assertTrue(utility.is_same_list(
            accumulate_cons,
            utility.list(1, 2, 3, 4, 5)))


if __name__ == '__main__':
    unittest.main()
