import unittest
from sorting_algorithms import bubble_sort
from ds import convert_to_linked_list

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.l1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.linked_list1 = convert_to_linked_list(self.l1)

    def test_bubble_sort_list(self):
        self.assertEqual(bubble_sort(self.l1), sorted(self.l1))

    def test_bubble_sort_linked_list(self):
        sorted_ll = bubble_sort(self.linked_list1)
        self.assertEqual(list(sorted_ll), sorted(self.l1))

if __name__ == "__main__":
    unittest.main()
