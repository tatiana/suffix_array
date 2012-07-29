# coding: utf-8
import unittest

from suffix import SuffixArray


class TestSuffixArray(unittest.TestCase):
    def setUp(self):
        text = 'tobeornottobe'
        self.suffix_array = SuffixArray(text)

    def test_tobeornottobe_bucket_sort(self):
        expected = {
            'b': [2, 11],
            'e': [3, 12],
            '$': [13],
            'o': [1, 4, 7, 10],
            'n': [6],
            'r': [5],
            't': [0, 8, 9]
        }
        self.suffix_array.bucket_sort()
        self.assertEqual(expected, self.suffix_array.group_dict)

    def test_tobeornottobe_phase1(self):
        expected = {
            'temp':   [13, 2, 11, 3, 12,  6, 1, 4,  7, 10,  5,  0,  8,  9],
            'group':  [0,  2,  2, 4,  4,  5, 9, 9,  9,  9, 10, 13, 13, 13],
            'gindex': [13, 9,  2, 4,  9, 10, 5, 9, 13, 13,  9,  2,  4,  0],
            'pending': {11: 3, 1: 2, 3: 2, 6: 4},
        }
        self.suffix_array.phase1()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp_array
        )
        self.assertEqual(
            expected['group'],
            self.suffix_array.group
        )
        self.assertEqual(
            expected['pending'],
            self.suffix_array.pending
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_index
        )

    def test_tobeornottobe_phase2(self):
        expected = {
            'temp': [13, 2, 11, 12, 3, 6, 1, 10, 4, 7, 5, 0, 9, 8],
            'group': [0, 2,  2,  3, 4, 5, 7, 7,  8, 9, 10, 12, 12, 13],
            'pending': {1: 2, 6: 2, 11: 2}
        }
        self.suffix_array.phase2()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp_array
        )
        self.assertEqual(
            expected['group'],
            self.suffix_array.group
        )
        self.assertEqual(
            expected['pending'],
            self.suffix_array.pending
        )

    # def test_tobeornottobe(self):
    #     self.assertEqual(
    #         self.suffix_array.process(),
    #         [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
    #     )

if __name__ == "__main__":
    unittest.main()


# temp[1] == 2
# temp[2] == 11

# group[1] == 2  # b
# group[2] == 2  # b

# pending[1] == 2 # dois elementos na posição 1 do temp
# group_of_next[1] = ['e', 'e']

# {2: 'e', 11: 'e'}

