import unittest
from src.main import sum


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)

    def test_sum_2(self):
        self.assertEqual(sum(2, 3), 5)

    def test_sum_3(self):
        self.assertEqual(sum(3, 4), 7)
