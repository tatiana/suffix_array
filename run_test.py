import pickle
import sys
import time

from os.path import exists, split, splitext
from benchmark.dataset import substring_size, get_random_substring_list,\
    LIST_SIZE
from suffix_array.lcp import compute_binary_search_path, compute_xlcp,\
    lcp_search
from suffix_array.search import suffix_binary_search
from suffix_array.suffix import create_suffix_array


text = ""
n = 0
suffix_array = []
llcp = []
rlcp = []
dataset_dict = []


def unpickle(filename):
    fp = open(filename, "r")
    data = pickle.load(fp)
    fp.close()
    return data


def picklefy(filename, data):
    fp = open(filename, "w")
    pickle.dump(data, fp)
    fp.close()


def load_text(filename):
    global text
    global n
    fp = open(filename, "r")
    text = fp.read()
    n = len(text)
    fp.close()


def load_suffix_array(fileprefix):
    suffix_array_filename = "%s_array.pck" % fileprefix
    global suffix_array
    global n

    print "Computing suffix array..."
    if exists(suffix_array_filename):
        print "    Reading suffix array from %s..." % suffix_array_filename
        suffix_array = unpickle(suffix_array_filename)
    else:
        print "    Creating suffix array..."
        suffix_array = create_suffix_array(filename)
        print "    Writing suffix array to %s..." % suffix_array_filename
        picklefy(filename, suffix_array)
        print "    Done."


def load_lcp_structures(fileprefix):
    llcp_filename = "%s_llcp.pck" % fileprefix
    rlcp_filename = "%s_rlcp.pck" % fileprefix
    global llcp
    global rlcp
    global n

    print "Pre-processing LCP search datastructures..."
    if exists(llcp_filename) and exists(rlcp_filename):
        print "    Reading llcp array from %s..." % llcp_filename
        llcp = unpickle(llcp_filename)
        print "    Reading rlcp array from %s..." % rlcp_filename
        rlcp = unpickle(rlcp_filename)
    else:
        print "    Computing binary search paths..."
        lm, m, rm = compute_binary_search_path(n)
        print "    Computing rlcp array..."
        rlcp = compute_xlcp(rm, m, suffix_array, text)
        print "    Writing rlcp array to %s..." % rlcp_filename
        picklefy(rlcp_filename, rlcp)
        print "    Computing llcp array..."
        llcp = compute_xlcp(lm, m, suffix_array, text)
        print "    Writing llcp array to %s..." % llcp_filename
        picklefy(llcp_filename, llcp)
        print "    Done."


def load_dataset(fileprefix):
    dataset_filename = "%s_dataset_dict.pck" % fileprefix
    global dataset_dict
    global text

    print "Loading dataset..."
    if exists(dataset_filename):
        print "    Reading dataset from %s..." % dataset_filename
        dataset_dict = unpickle(dataset_filename)
    else:
        print "    Computing dataset..."
        dataset_dict = {}
        for i in xrange(1, 11):
            item_size = substring_size(i)
            dataset_dict[i] = get_random_substring_list(\
                text, LIST_SIZE, item_size)
        print "    Writing dataset to %s..." % dataset_filename
        picklefy(dataset_filename, dataset_dict)
        print "    Done."


def search_dataset(search_type):
    print "Searching dataset..."
    sorted_keys = sorted(dataset_dict.keys())
    for key in sorted_keys:
        total_time = 0
        dataset = dataset_dict[key]
        for substring in dataset:
            i = time.time()
            if search_type == "lcp":
                answer = lcp_search(text, suffix_array, substring, llcp, rlcp)
            else:
                answer = suffix_binary_search(text, suffix_array, substring)
            f = time.time()
            assert substring == text[answer: answer + len(substring)]
            total_time += f - i

        print "    key: %2d |  total time: %f | average time: %f" %\
            (key, total_time, total_time / LIST_SIZE)
    print "Done."


def main(filename="corpus/bible.txt", search_type="binary"):
    fileprefix = splitext(split(filename)[-1])[0]
    load_text(filename)
    load_suffix_array(fileprefix)
    load_dataset(fileprefix)
    if search_type == "lcp":
        load_lcp_structures(fileprefix)
    search_dataset(search_type)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        search_type = sys.argv[-2]
        filename = sys.argv[-1]
    else:
        print "Usage:"
        print "python run_test.py <search_type> <filepath>"
        print "    <search>: binary or lcp"
        print "    <filepath>: corpus/bible.txt or corpus/world192.txt"
        exit()

    print "Processing %s..." % filename
    main(filename, search_type)


#import cProfile
#cProfile.run("main()", "result")
#import pstats
#stats = pstats.Stats('result')
#stats.sort_stats('cumulative').print_stats(10)
#stats.sort_stats('time').print_stats(10)
#import pdb; pdb.set_trace()

# add @profile decorator
# kernprof.py -l run_test.py
# python -m line_profiler run_test.py.lprof
