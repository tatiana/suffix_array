# coding: utf-8
import unittest

from suffix_array.suffix import SuffixArray, DOLLAR


class TestToBeOrNotToBeSuffixArray(unittest.TestCase):

    def setUp(self):
        text = 'tobeornottobe'
        self.suffix_array = SuffixArray(text)

    def test_tobeornottobe_bucket_sort(self):
        expected = {
            'b': [2, 11],
            'e': [3, 12],
            DOLLAR: [13],
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
        self.assertEqual(
           expected['group'],
           self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_tobeornottobe_iterate1(self):
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
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_tobeornottobe_iterate2(self):
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
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_tobeornottobe_iterate3(self):
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
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
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


class TestAbracadabraSuffixArray(unittest.TestCase):

    def setUp(self):
        text = 'abracadabra'
        self.suffix_array = SuffixArray(text)

    def test_abracadabra_bucket_sort(self):
        expected = {
            DOLLAR: [11],
            'a': [0, 3, 5, 7, 10],
            'b': [1, 8],
            'c': [4],
            'd': [6],
            'r': [2, 9]
        }
        self.suffix_array.bucket_sort()
        computed = self.suffix_array.items_by_bucket
        self.assertEqual(computed, expected)

    def test_abracadabra_setup(self):
        expected = {
            'temp':   [11, 0,  3,  5, 7, 10, 1, 8, 4,  6, 2,   9],
            'group':  [0,  5,  5,  5, 5,  5, 7, 7, 8,  9, 11, 11],
            'gindex': [5,  7, 11,  5, 8,  5, 9, 5, 7, 11,  5,  0],
            'unsorted': {1: 5, 6: 2, 10: 2},
        }
        self.suffix_array.setup()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        self.assertEqual(
           expected['group'],
           self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_abracadabra_iterate1(self):
        expected = {  # a   b   r   a   c   a   d   a   b   r   a   $
            #         [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]
            'temp':   [11, 10,  0,  7,  3,  5,  1,  8,  4,  6,  2,  9],
            'group':  [ 0,  1,  3,  3,  4,  5,  7,  7,  8,  9, 11, 11],
            'gindex': [ 3,  7, 11,  4,  8,  5,  9,  3,  7, 11,  1,  0],
            'unsorted': {2: 2, 6: 2, 10: 2},
        }
        self.suffix_array.setup()
        self.suffix_array.iterate()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_abracadabra_iterate2(self):
        #text = 'abracadabra'
        #       '01234567890'
        # 11  $   0
        # 10  a$  0
        # 7   abra$   1
        # 0   abracadabra$    4
        # 3   acadabra$   1
        # 5   adabra$ 1
        # 8   bra$    0
        # 1   bracadabra$ 3
        # 4   cadabra$    0
        # 6   dabra$  0
        # 9  ra$ 0
        # 2   racadabra$  2
        expected = {  # a   b   r   a   c   a   d   a   b   r   a   $
            #         [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]
            'temp':   [11, 10,  0,  7,  3,  5,  8,  1,  4,  6,  9,  2],
            'group':  [ 0,  1,  3,  3,  4,  5,  6,  7,  8,  9, 10, 11],
            'gindex': [ 3,  7, 11,  4,  8,  5,  9,  3,  6, 10,  1,  0],
            'unsorted': {2: 2},
        }
        self.suffix_array.setup()
        self.suffix_array.iterate()
        self.suffix_array.iterate()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )


    # TODO: write test for iterate3

    def test_abracadabra(self):
        self.assertEqual(
            self.suffix_array.process(),
            [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
       )


class TestSeq_1_13_SuffixArray(unittest.TestCase):

    def setUp(self):
        text = '12345678910111213'
        self.suffix_array = SuffixArray(text)

    def test_12345678910111213_setup(self):
        expected = {
             'temp':   [17, 10,  0,  9, 11, 12, 13, 15,  1, 14,  2, 16,  3,  4,  5,  6,  7,  8],
             'group':  [0,   1,  7,  7,  7,  7,  7,  7,  9,  9, 11, 11, 12, 13, 14, 15, 16, 17],
             'gindex': [7,   9, 11, 12, 13, 14, 15, 16, 17,  7,  1,  7,  7,  7,  9,  7, 11,  0],
             'unsorted': {2: 6, 8: 2, 10: 2}
        }
        self.suffix_array.setup()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_12345678910111213_iterate1(self):
        expected = {
             'temp':   [17, 10,  9, 11, 12,  0, 13, 15, 14,  1, 16,  2,  3,  4,  5,  6,  7,  8],
             'group':  [0,   1,  2,  4,  4,  6,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17],
             'gindex': [6,   9, 11, 12, 13, 14, 15, 16, 17,  2,  1,  4,  4,  6,  8,  7, 10,  0],
             'unsorted': {3: 2, 5: 2}
        }
        self.suffix_array.setup()
        self.suffix_array.iterate()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )

    def test_12345678910111213_iterate2(self):
        expected = {
             'temp':   [17, 10,  9, 11, 12,  13, 0, 15, 14,  1, 16,  2,  3,  4,  5,  6,  7,  8],
             'group':  [0,   1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17],
             'gindex': [6,   9, 11, 12, 13, 14, 15, 16, 17,  2,  1,  3,  4,  5,  8,  7, 10,  0],
             'unsorted': {}
        }
        self.suffix_array.setup()
        self.suffix_array.iterate()
        self.suffix_array.iterate()
        self.assertEqual(
            expected['temp'],
            self.suffix_array.temp
        )
        self.assertEqual(
            expected['group'],
            self.suffix_array.group_by_temp_index
        )
        self.assertEqual(
            expected['unsorted'],
            self.suffix_array.unsorted
        )
        self.assertEqual(
            expected['gindex'],
            self.suffix_array.group_by_text_index
        )


if __name__ == "__main__":
    unittest.main()
