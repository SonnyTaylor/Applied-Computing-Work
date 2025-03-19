import unittest
from search_sort import binary_search, quicksort


class TestSearchSort(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.sorted_list = ["A", "B", "C", "D", "E"]
        self.numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]

    def test_binary_search_existing(self):
        """Test binary search with existing items"""
        self.assertEqual(binary_search(self.sorted_list, "A"), 0)
        self.assertEqual(binary_search(self.sorted_list, "C"), 2)
        self.assertEqual(binary_search(self.sorted_list, "E"), 4)

    def test_binary_search_nonexistent(self):
        """Test binary search with non-existent items"""
        self.assertEqual(binary_search(self.sorted_list, "X"), -1)
        self.assertEqual(binary_search(self.sorted_list, "0"), -1)
        self.assertEqual(binary_search(self.sorted_list, "Z"), -1)

    def test_binary_search_empty(self):
        """Test binary search with empty list"""
        self.assertEqual(binary_search([], "A"), -1)

    def test_quicksort_numbers(self):
        """Test quicksort with numbers"""
        sorted_numbers = quicksort(self.numbers, lambda x: x)
        self.assertEqual(sorted_numbers, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quicksort_strings(self):
        """Test quicksort with strings"""
        unsorted_strings = ["C", "A", "B", "E", "D"]
        sorted_strings = quicksort(unsorted_strings, lambda x: x)
        self.assertEqual(sorted_strings, ["A", "B", "C", "D", "E"])

    def test_quicksort_empty(self):
        """Test quicksort with empty list"""
        self.assertEqual(quicksort([], lambda x: x), [])

    def test_quicksort_single_item(self):
        """Test quicksort with single item"""
        self.assertEqual(quicksort([1], lambda x: x), [1])

    def test_quicksort_duplicates(self):
        """Test quicksort with duplicate items"""
        numbers_with_duplicates = [3, 1, 3, 2, 3, 4, 3]
        sorted_numbers = quicksort(numbers_with_duplicates, lambda x: x)
        self.assertEqual(sorted_numbers, [1, 2, 3, 3, 3, 3, 4])


if __name__ == "__main__":
    unittest.main()
