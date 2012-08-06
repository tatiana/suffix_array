import pickle
import time

from benchmark.dataset import substring_size, get_random_substring_list,\
    LIST_SIZE
from suffix_array.search import suffix_binary_search, lcp_search

fp = open("bible_array.pck", "r")
suffix_array = pickle.load(fp)
fp.close()

filename = "corpus/bible.txt"
fp = open(filename, "r")
text = fp.read()
fp.close()

# dataset_dict = {}
# for i in xrange(1, 11):
#     item_size = substring_size(i)
#     dataset_dict[i] = get_random_substring_list(text, LIST_SIZE, item_size)
#     #dataset = get_random_substring_list(text, LIST_SIZE, item_size)
def main():
    fp = open("bible_dataset_dict.pck", "r")
    dataset_dict = pickle.load(fp)
    fp.close()

    sorted_keys = sorted(dataset_dict.keys())
    for key in [sorted_keys[0]]:
        print "######################"
        print "key: ", key
        total_time = 0
        dataset = dataset_dict[key]
        for substring in dataset:
            i = time.time()
            print substring
            answer = lcp_search(text, suffix_array, substring)
            f = time.time()
            assert substring == text[answer: answer + len(substring)]
            print f - i,  answer
            total_time += f - i


import profile
profile.run("main()")
    #print "total time: ", total_time
    #print "average time: ", total_time / LIST_SIZE
# 2468358

# substring = "ith t"
# print suffix_binary_search(text, suffix_array, substring)
# i = time.time()
# print substring
# answer = lcp_search(text, suffix_array, substring)
# f = time.time()
# assert substring == text[answer: answer + len(substring)]
# print f - i,  answer
