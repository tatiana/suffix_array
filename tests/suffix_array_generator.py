# Example of how to use:
# python tests/suffix_array_generator.py corpus/abracadabra.txt

import sys

DOLLAR = chr(0)


def create_suffix_array(text):
    text = "%s%s" % (text, DOLLAR)
    suffixes = [text[i:] for i in xrange(len(text))]
    suffixes.sort()
    return [text.find(suffix) for suffix in suffixes]


def test_create_suffix_array():
    text = "abracadabra"
    suffix_array_expected = [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
    suffix_array_computed = create_suffix_array(text)
    assert suffix_array_expected == suffix_array_computed


if __name__ == "__main__":
    # let's test if it is working:
    test_create_suffix_array()

    # run for provided filename
    filename = sys.argv[-1]
    fp = open(filename, "r")
    text = fp.read()
    print create_suffix_array(text)
