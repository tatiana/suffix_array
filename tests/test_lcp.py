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

#                            4 (0, 9)
#        2 (0, 4)                            6 (4, 9)
#    1 (0, 2)    3 (2, 4)                5 (4, 6)    7 (6, 9)
#0 (0, 1) 1 (1, 2) 2 (2, 3) 3 (3, 4)    4 (4, 5) 5 (5, 6) 6 (6, 7) 8 (7, 9)

    def test_binary_search_path_n_equals_10(self):
        n = 10
        lm = [0, 0, 2, 0, 4, 4, 6, 7]
        rm = [2, 4, 4, 9, 6, 9, 9, 9]
        m = [1, 2, 3, 4, 5, 6, 7, 8]
        (new_lm, new_m, new_rm) = compute_binary_search_path(n)
        self.assertEquals(new_lm, lm)
        self.assertEquals(new_rm, rm)
        self.assertEquals(new_m, m)

if __name__ == "__main__":
    unittest.main()
