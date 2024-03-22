import unittest
from poetry_demo.custom_sum import custom_sum

class TestCustomSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(custom_sum([]), 0)

    def test_single_item_list(self):
        self.assertEqual(custom_sum([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(custom_sum([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(custom_sum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(custom_sum([1, -2, 3, -4]), -3)

if __name__ == '__main__':
    unittest.main()
