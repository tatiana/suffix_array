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
            '\x00': [13],
            'o': [1, 4, 7, 10],
            'n': [6],
            'r': [5],
            't': [0, 8, 9]
        }
        self.suffix_array.bucket_sort()
        computed = self.suffix_array.items_by_bucket
        self.assertEqual(computed, expected)

    def test_tobeornottobe_setup(self):
        expected = {
            'temp':   [13, 2, 11, 3, 12,  6, 1, 4,  7, 10,  5,  0,  8,  9],
            'group':  [0,  2,  2, 4,  4,  5, 9, 9,  9,  9, 10, 13, 13, 13],
            'gindex': [13, 9,  2, 4,  9, 10, 5, 9, 13, 13,  9,  2,  4,  0],
            'unsorted': {11: 3, 1: 2, 3: 2, 6: 4},
        }
        self.suffix_array.setup()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        #self.assertEqual(
        #    expected['group'],
        #    self.suffix_array.group_by_temp_index
        #)
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_tobeornottobe_iterate(self):
        expected = {
            'temp':   [13, 2, 11, 12, 3, 6,  1, 10, 4, 7, 5, 0, 9, 8],
            'group':  [0,  2,  2,  3, 4, 5,  7, 7,  8, 9, 10, 12, 12, 13],
            'gindex': [12, 7,  2, 4,  8, 10, 5, 9, 13, 12, 7,  2,  3,  0],
            'unsorted': {1: 2, 6: 2, 11: 2}
        }
        self.suffix_array.setup()
        self.suffix_array.iterate()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        # self.assertEqual(
        #     expected['group'],
        #     self.suffix_array.group_by_temp_index
        # )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_tobeornottobe_phase3(self):
        expected = {
            'temp':   [13, 11, 2, 12, 3,  6, 10, 1,  4,  7,  5,  0,  9, 8],
            'group':  [0,   1, 2,  3, 4,  5,  6, 7,  8,  9, 10, 12, 12, 13],
            'gindex': [12,  7, 2,  4, 8, 10,  5, 9, 13, 12,  6,  1,  3, 0],
            'unsorted': {11: 2}
        }
        self.suffix_array.setup()
        self.suffix_array.iterate()
        self.suffix_array.iterate()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        # self.assertEqual(
        #     expected['group'],
        #     self.suffix_array.group_by_temp_index
        # )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_tobeornottobe_phase4(self):
        expected = {
            'temp':   [13, 11, 2, 12,  3, 6, 10,  1,  4, 7,  5,  9,  0, 8],
            'group':  [0,  1,  2,  3,  4, 5,  6,  7,  8, 9, 10, 11, 12, 13],
            'gindex': [12, 7,  2,  4,  8, 10, 5,  9, 13, 11, 6,  1,  3, 0],
            'unsorted': {}
        }
        self.suffix_array.setup()
        self.suffix_array.iterate()
        self.suffix_array.iterate()
        self.suffix_array.iterate()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        # self.assertEqual(
        #     expected['group'],
        #     self.suffix_array.group_by_temp_index
        # )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_tobeornottobe(self):
        self.assertEqual(
            self.suffix_array.process(),
            [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
        )

    # def test_world(self):
    #     import time
    #     i = time.time()
    #     fp = open("corpus/world192.txt")
    #     f = time.time()
    #     text = fp.read()
    #     print "read time:", (f - i)
    #     self.suffix_array = SuffixArray(text)
    #     self.suffix_array.process()
    #     print "process time:", (f - i)


if __name__ == "__main__":
    unittest.main()
