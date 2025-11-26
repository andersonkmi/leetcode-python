import unittest
from two_pointers import pair_sum_sorted_brute_force

class TestTwoPointers(unittest.TestCase):
    def test_pair_sum_brute_force_when_array_empty_return_empty(self):
        numbers = []
        target = 7
        result = pair_sum_sorted_brute_force(numbers, target)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()