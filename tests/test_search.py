import unittest
from suffix_array.search import binary_search, substring_binary_search,\
    suffix_binary_search


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


class SubstringBinarySearchTestCase(unittest.TestCase):

    def test_substring_binary_search_empty_text(self):
        text = ""
        substring = "$"
        expected = -1
        computed = substring_binary_search(text, substring)
        self.assertEquals(computed, expected)

    def test_substring_binary_search_with_1_char_substring(self):
        text = "abc"
        substring = "c"
        expected = 2
        computed = substring_binary_search(text, substring)
        self.assertEquals(computed, expected)

    def test_substring_binary_search_without_1_char_substring(self):
        text = "abc"
        substring = "d"
        expected = -1
        computed = substring_binary_search(text, substring)
        self.assertEquals(computed, expected)

    def test_substring_binary_search_with_2_chars_substring(self):
        text = "defg"
        substring = "ef"
        expected = 1
        computed = substring_binary_search(text, substring)
        self.assertEquals(computed, expected)

    def test_substring_binary_search_without_2_chars_substring(self):
        text = "hijk"
        substring = "lmn"
        expected = -1
        computed = substring_binary_search(text, substring)
        self.assertEquals(computed, expected)


class SuffixArrayBinarySearchTestCase(unittest.TestCase):

    def test_suffix_binary_search_abracadabra_contains_cada(self):
        text = "abracadabra$"
        suffix_array = [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
        substring = "cada"
        expected = 4
        computed = suffix_binary_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_suffix_binary_search_abracadabra_doesnt_contain_abrax(self):
        text = "abracadabra$"
        suffix_array = [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
        substring = "abrax"
        expected = -1
        computed = suffix_binary_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_suffix_binary_search_tobeornottobe_contains_tobe(self):
        text = "tobeornottobe$"
        suffix_array = [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
        substring = "tobe"
        expected = 9
        computed = suffix_binary_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_suffix_binary_search_tobeornottobe_doesnt_contain_abc(self):
        text = "tobeornottobe$"
        suffix_array = [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
        substring = "abc"
        expected = -1
        computed = suffix_binary_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_suffix_binary_search_tobeornottobe_contains_tobeornottobe(self):
        text = "tobeornottobe$"
        suffix_array = [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
        substring = "tobeornottobe$"
        expected = 0
        computed = suffix_binary_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)


if __name__ == "__main__":
    unittest.main()
