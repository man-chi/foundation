import unittest
from src.main import sum


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)