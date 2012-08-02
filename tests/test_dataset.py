import unittest

from benchmark.dataset import get_random_list_of_indexes, get_substring_list,\
    get_random_substring_list, substring_size


class DatasetTestCase(unittest.TestCase):

    def test_substring_size_for_1_is_5(self):
        i = 1
        expected = 5
        computed = substring_size(i)
        self.assertEquals(computed, expected)

    def test_substring_size_for_2_is_10(self):
        i = 2
        expected = 10
        computed = substring_size(i)
        self.assertEquals(computed, expected)

    def test_substring_size_for_3_is_20(self):
        i = 3
        expected = 20
        computed = substring_size(i)
        self.assertEquals(computed, expected)

    def test_get_random_list_of_indexes(self):
        computed_list = get_random_list_of_indexes(
            list_size=2,
            string_size=10,
            substring_size=3)

        self.assertEquals(len(computed_list), 2)
        self.assertTrue(-1 < computed_list[0] < 8)
        self.assertTrue(-1 < computed_list[1] < 8)

    def test_get_substring_list(self):
        computed_list = get_substring_list(
            string="I think therefore I am",
            indexes=[2, 8],
            substring_size=5)
        expected_list = ["think", "there"]
        self.assertEquals(computed_list, expected_list)

    def test_get_random_substring_list(self):
        text = "Welcome to where time stands still"
        computed_list = get_random_substring_list(
            string=text,
            list_size=3,
            substring_size=6
        )
        self.assertEquals(len(computed_list), 3)
        self.assertEquals(len(computed_list[0]), 6)
        self.assertEquals(len(computed_list[1]), 6)
        self.assertEquals(len(computed_list[2]), 6)
        self.assertTrue(computed_list[0] in text)
        self.assertTrue(computed_list[1] in text)
        self.assertTrue(computed_list[2] in text)
