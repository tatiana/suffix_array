DOLLAR = chr(0)


class SuffixArray(object):

    def __init__(self, text):
        self._delta = 1
        self.text = "%s%s" % (text, DOLLAR)
        self.temp = []  # suffix array under development

        self.items_by_bucket = {}  # used by bucket sort and initial setup
        # [suffix_first_char] => list of suffixes (represented by first pos)
        # by convention, groups are represented by last group item's index

        #self.group_by_temp_index = []
        # [index in temp] => group (represented by last item pos)
        # by convention, groups are represented by last group item's index
        # TODO: Delete me!

        self.group_by_text_index = [None] * len(self.text)
        # [index in text] => group (represented by last item pos)

        self.unsorted = {}  # suffixes that still need to be sorted
        # [index in temp] => number of items

    def bucket_sort(self, text=None):
        "Split suffixes into buckets according to their 1st char: O(n)"
        if text is None:
            text = self.text
        self.items_by_bucket = {}
        for suffix_pos, suffix_first_char in enumerate(text):
            index = suffix_first_char
            self.items_by_bucket[index] = self.items_by_bucket.get(index, [])
            self.items_by_bucket[index] += [suffix_pos]

    def setup(self):
        "Create initial array - partially sorted by 1st char: O(n)"
        self.bucket_sort()  # O(n)
        sorted_buckets = sorted(self.items_by_bucket.keys())
        index = 0
        for bucket in sorted_buckets:  # O(n)
            bucket_items = self.items_by_bucket[bucket]
            len_bucket = len(bucket_items)

            init_bucket = index
            if len_bucket != 1:
                self.unsorted[init_bucket] = len_bucket

            end_bucket = index + len_bucket - 1
            for init_suffix in bucket_items:  # O(m) where m = # items of bucket
                group = end_bucket
                self.group_by_text_index[init_suffix] = group
                #self.group_by_temp_index.append(group)  # TODO: Delete me!
            index += len_bucket
            self.temp += bucket_items

    def iterate(self):
        "Improve sorting based on the next char of each suffix: O(n)"

        # for each unsorted group of suffixes, try to sort by next char's group
        for init_group, len_group in self.unsorted.items():
            next_char = {}
            items = self.temp[init_group: init_group + len_group]
            for init_suffix in items:
                index = init_suffix
                next_char[index] = self.group_by_text_index[index + self._delta]

            # sort group suffixes by next char and update self.temp
            end_group = init_group + len_group - 1
            sorted_items = sorted(next_char, key=next_char.get)  # O(m.log(m))
            self.temp[init_group: end_group + 1] = sorted_items

            # if group items order changed, update auxiliary data structures
            if items != sorted_items:
                self.unsorted.pop(init_group)
                len_unsorted = 1

                # update groups according to new sorting, in a reverse loop
                # the group of the last item stays the same - so we only update
                # others
                for index in xrange(end_group - 1, init_group - 1, -1):
                    current_suffix = self.temp[index]
                    next_suffix = self.temp[index + 1]
                    if next_char[current_suffix] != next_char[next_suffix]:
                        current_group = index
                        if len_unsorted > 1:
                            self.unsorted[index + 1] = len_unsorted  # FIXME (+1)
                            len_unsorted = 1
                    else:
                        current_group = self.group_by_text_index[next_suffix]
                        len_unsorted += 1

                    #self.group_by_temp_index[index] = current_group
                    self.group_by_text_index[current_suffix] = current_group

                    if len_unsorted > 1:
                        self.unsorted[index] = len_unsorted

        self._delta *= 2


    def process(self):
        self.setup()
        while self.unsorted:
            self.iterate()
        return self.temp
