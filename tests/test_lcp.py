import unittest
from suffix_array.lcp import compute_binary_search_path


class BinarySearchPathTestCase(unittest.TestCase):

    def test_binary_search_path_n_equals_9(self):
        n = 9
        lm = [0, 0, 2, 0, 4, 4, 6]
        rm = [2, 4, 4, 8, 6, 8, 8]
        m = [1, 2, 3, 4, 5, 6, 7]
        (new_lm, new_m, new_rm) = compute_binary_search_path(n)
        self.assertEquals(new_lm, lm)
        self.assertEquals(new_rm, rm)
        self.assertEquals(new_m, m)


if __name__ == "__main__":
    unittest.main()
