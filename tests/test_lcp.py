import unittest
from benchmark.dataset import get_random_substring_list
from suffix_array.lcp import compute_binary_search_path, compute_lcp_array,\
    simple_lcp_search, longest_common_prefix
from suffix_array.suffix import SuffixArray


fixture_text =\
"""
We produce about one million dollars for each hour we work.  One
hundred hours is a conservative estimate for how long it we take
to get any etext selected, entered, proofread, edited, copyright
searched and analyzed, the copyright letters written, etc.  This
projected audience is one hundred million readers.  If our value
per text is nominally estimated at one dollar, then we produce a
million dollars per hour; next year we will have to do four text
files per month, thus upping our productivity to two million/hr.
The Goal of Project Gutenberg is to Give Away One Trillion Etext
Files by the December 31, 2001.  [10,000 x 100,000,000=Trillion]
This is ten thousand titles each to one hundred million readers.

Illicit drugs: There are five categories of illicit drugs - narcotics,
stimulants, depressants (sedatives), hallucinogens, and cannabis. These
categories include many drugs legally produced and prescribed by doctors as
well as those illegally produced and sold outside medical channels.

Cannabis (Cannabis sativa) is the common hemp plant, which provides
hallucinogens with some sedative properties, and includes marijuana (pot,
Acapulco gold, grass, reefer), tetrahydrocannabinol (THC, Marinol), hashish
(hash), and hashish oil (hash oil).

Coca (Erythroxylon coca) is a bush, and the leaves contain the stimulant
cocaine. Coca is not to be confused with cocoa, which comes from cacao seeds
and is used in making chocolate, cocoa, and cocoa butter.

Cocaine is a stimulant derived from the leaves of the coca bush.

Depressants (sedatives) are drugs that reduce tension and anxiety and include
chloral hydrate, barbiturates (Amytal, Nembutal, Seconal, phenobarbital),
benzodiazepines (Librium, Valium), methaqualone (Quaalude), glutethimide
(Doriden), and others (Equanil, Placidyl, Valmid).

l
ships' registrations. Registration of a ship provides it with a nationality
and makes it subject to the laws of the country in which registered (the flag
state) regardless of the nationality of the ship's ultimate owner.

Money figures: All are expressed in contemporaneous US dollars unless
otherwise indicated.

Net migration rate: The balance between the number of persons entering and
leaving a country during the year per 1,000 persons (based on midyear
population). An excess of persons entering the country is referred to as net
immigration (3.56 migrants/1,000 population); an excess of persons leaving the
country as net emigration (-9.26 migrants/1,000 population).

Population: Figures are estimates from the Bureau of the Census based on
statistics from population censuses, vital registration systems, or sample
surveys pertaining to the recent past, and on assumptions about future trends.
"""


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


class SuffixArrayLCPSearchTestCase(unittest.TestCase):

    def test_simple_lcp_search_abracadabra_contains_cada(self):
        text = "abracadabra$"
        suffix_array = [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
        substring = "cada"
        expected = 4
        computed = simple_lcp_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_simple_lcp_search_abracadabra_doesnt_contain_abrax(self):
        text = "abracadabra$"
        suffix_array = [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
        substring = "abrax"
        expected = -1
        computed = simple_lcp_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_simple_lcp_search_tobeornottobe_contains_tobe(self):
        text = "tobeornottobe$"
        suffix_array = [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
        substring = "tobe"
        expected = 9
        computed = simple_lcp_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_simple_lcp_search_tobeornottobe_doesnt_contain_abc(self):
        text = "tobeornottobe$"
        suffix_array = [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
        substring = "abc"
        expected = -1
        computed = simple_lcp_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_simple_lcp_search_tobeornottobe_contains_tobeornottobe(self):
        text = "tobeornottobe$"
        suffix_array = [13, 11, 2, 12, 3, 6, 10, 1, 4, 7, 5, 9, 0, 8]
        substring = "tobeornottobe$"
        expected = 0
        computed = simple_lcp_search(text, suffix_array, substring)
        self.assertEquals(computed, expected)

    def test_brutal_test(self):
        text = fixture_text
        suffix_array = SuffixArray(text)
        array = suffix_array.process()

        substrings = [\
        ',\nstimulants, depres',
         'f a ship provides it']

        for substring in substrings:
            answer = simple_lcp_search(text, array, substring)
            self.assertEquals(substring, text[answer: answer + len(substring)])


class LCPTestCase(unittest.TestCase):

    def test_longest_common_prefix_empty_string(self):
        string1 = ''
        string2 = 'other string is empty :/'
        response = longest_common_prefix(string1, string2)
        expected = 0
        self.assertEquals(response, expected)

    def test_longest_common_prefix_different_sizes(self):
        string1 = 'cada'
        string2 = 'cadabra$'
        response = longest_common_prefix(string1, string2)
        expected = 4
        self.assertEquals(response, expected)

    def test_longest_common_prefix_python_phrases(self):
        string1 = 'python rocks'
        string2 = 'python is cool'
        response = longest_common_prefix(string1, string2)
        expected = 7
        self.assertEquals(response, expected)

    def test_longest_common_prefix_python_phrases_inverted(self):
        string1 = 'python is cool'
        string2 = 'python rocks'
        response = longest_common_prefix(string1, string2)
        expected = 7
        self.assertEquals(response, expected)

    def test_nothing_in_common(self):
        string1 = 'nothing in'
        string2 = 'common'
        response = longest_common_prefix(string1, string2)
        expected = 0
        self.assertEquals(response, expected)


class LCPArrayTestCase(unittest.TestCase):

    def test_get_lcp_array_for_abracadabra(self):
        text = "abracadabra$"
        suffix_array = [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
        lcp_array_expected = [0, 0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]
        lcp_array_computed = compute_lcp_array(text, suffix_array)
        self.assertEquals(lcp_array_computed, lcp_array_expected)

    def test_get_lcp_array_for_mississipi(self):
        text = "mississippi$"
        suffix_array = [11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
        lcp_array_expected = [0, 0, 1, 1, 4, 0, 0, 1, 0, 2, 1, 3]
        lcp_array_computed = compute_lcp_array(text, suffix_array)
        self.assertEquals(lcp_array_computed, lcp_array_expected)

    def test_get_lcp_array_raises_exception_if_wrong_input(self):
        text = "wrong input text"
        suffixes = []
        self.assertRaises(AssertionError, compute_lcp_array, text, suffixes)


if __name__ == "__main__":
    unittest.main()
