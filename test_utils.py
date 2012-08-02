import unittest
from utils import binary_search


class BinarySearchTestCase(unittest.TestCase):

    def test_binary_search_empty(self):
        array = []
        value = 1
        expected = -1
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_1_sized_array_without_value(self):
        array = [3]
        value = 2
        expected = -1
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_1_sized_array_with_value(self):
        array = [4]
        value = 4
        expected = 0
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_2_sized_array_without_value(self):
        array = [5, 6]
        value = 7
        expected = -1
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_2_sized_array_with_value(self):
        array = [8, 9]
        value = 9
        expected = 1
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_4_sized_array_without_value(self):
        array = [10, 11, 12, 13]
        value = 14
        expected = -1
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_4_sized_array_with_value(self):
        array = [14, 15, 16, 17]
        value = 16
        expected = 2
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_7_sized_array_without_value(self):
        array = [20, 21, 22, 23, 24, 25, 26]
        value = 19
        expected = -1
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

    def test_binary_search_7_sized_array_with_value(self):
        array = [37, 36, 35, 34, 32, 31, 33]
        value = 34
        expected = 3
        computed = binary_search(array, value)
        self.assertEquals(computed, expected)

if __name__ == "__main__":
    unittest.main()
