import unittest


class TestMathDojo(unittest.TestCase):
    def test_add_single_number(self):
        # md = MathDojo()
        result = md.add(5).result
        self.assertEqual(result, 5)

    def test_add_multiple_numbers(self):
        # md = MathDojo()
        result = md.add(2, 3, 4).result
        self.assertEqual(result, 9)

    def test_subtract_single_number(self):
        # md = MathDojo()
        md.result = 10  # start with 10
        result = md.subtract(3).result
        self.assertEqual(result, 7)

    def test_subtract_multiple_numbers(self):
        # md = MathDojo()
        md.result = 20
        result = md.subtract(5, 5, 5).result
        self.assertEqual(result, 5)

    def test_chain_methods(self):
        # md = MathDojo()
        result = md.add(2).add(2, 5, 1).subtract(3, 2).result
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self
        # create an instance:
md = MathDojo()
