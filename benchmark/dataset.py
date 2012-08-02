# howto run:
# python benchmark/dataset.py corpus/world192.txt

import sys
from random import random

LIST_SIZE = 1000


substring_size = lambda i: 5 * (2 ** (i - 1))


def get_random_list_of_indexes(list_size, string_size, substring_size):
    last_feasible_index = string_size - substring_size
    return [int((last_feasible_index) * random()) for i in xrange(list_size)]


def get_substring_list(string, indexes, substring_size):
    return [string[index: index + substring_size] for index in indexes]


def get_random_substring_list(string, list_size, substring_size):
    indexes = get_random_list_of_indexes(
        list_size=list_size,
        string_size=len(string),
        substring_size=substring_size
        )
    substrings = get_substring_list(
        string=string,
        indexes=indexes,
        substring_size=substring_size)
    return substrings


if __name__ == "__main__":
    filename = sys.argv[-1]
    fp = open(filename, "r")
    text = fp.read()
    dataset = {}
    for i in xrange(1, 11):
        item_size = substring_size(i)
        dataset[i] = get_random_substring_list(text, LIST_SIZE, item_size)
    # result in dataset \o/
