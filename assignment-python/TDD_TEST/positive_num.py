import unittest


class test_positive_num(unittest.TestCase):

    def is_positive(self):
        self.assertEqual(True, isPositive(3))

    def is_negative(self):
        self.assertEqual(False, isPositive(-3))


if __name__ == "__main__":
    unittest.main()


def isPositive(n):
    return n > 0




