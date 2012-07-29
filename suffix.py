class SuffixArray(object):
    def __init__(self, text):
        self._index = 1

        self.text = "%s$" % text
        self.temp_array = []  # suffix array wanna be
        self.group = []  # values based on self.temp_array order
        self.group_dict = {}  # letter of group: list of indexes
        self.group_by_index = [None] * len(self.text)  # based on original self.text
        self.pending = {}  # index in temp_array: number of items to be sorted
        self.group_of_next = {}  # index in temp_array: next letters of items

    def bucket_sort(self, text=None):
        if text is None:
            text = self.text
        self.group_dict = {}
        for pos, char in enumerate(text):
            index = char
            self.group_dict[index] = self.group_dict.get(index, [])
            self.group_dict[index] += [pos]

    def phase1(self):
        self.bucket_sort()
        group_indexes = sorted(self.group_dict.keys())
        last_item_index = 0
        for char in group_indexes:
            items = self.group_dict[char]
            n_items = len(items)
            last_item_index += n_items

            index_in_pending = len(self.group)
            if n_items == 1:
                self.group_dict.pop(char)
            else:
                self.pending[index_in_pending] = n_items

            for i in items:
                self.group_by_index[i] = last_item_index - 1
                self.group.append(last_item_index - 1)

            self.temp_array += items

    def phase2(self):
        self.phase1()
        for index, n_items in self.pending.items():
            group_of_next = {}
            array = self.temp_array[index: index + n_items]
            for value in array:
                group_of_next[value] = self.group_by_index[value + self._index]
            sorted_items = sorted(group_of_next, key=group_of_next.get)
            self.temp_array[index: index + n_items] = sorted_items


            if array != sorted_items:
                # update self.pending
                self.pending.pop(index)
                new_pending_group_items = 1

                # update self.group
                last_index = self.group[index]

                for current_index in xrange(last_index - 1, last_index - n_items, -1):
                    if group_of_next[self.temp_array[current_index]] != group_of_next[self.temp_array[current_index + 1]]:
                        self.group[current_index] = current_index
                        if new_pending_group_items > 1:
                            self.pending[current_index + 1] = new_pending_group_items
                        new_pending_group_items = 1
                    else:
                        self.group[current_index] = self.group[current_index + 1]
                        new_pending_group_items += 1

                    if new_pending_group_items > 1:
                        self.pending[current_index] = new_pending_group_items



            # index_in_pending = len(self.group)
            # if n_items != 1:
            #     self.pending.pop(char)
            # else:
            #     self.pending[index_in_pending] = n_items

        self._index *= 2

        # group_indexes = sorted(self.group_dict.keys())
        # for i in self.pending:
        #     pass
        # last_item_index = 0
        # for index in group_indexes:
        #     items = self.group_dict[index]
        #     n_items = len(items)
        #     last_item_index += n_items

        #     for i in items:
        #         self.group.append(last_item_index - 1)

        #     self.temp_array += items

    def process(self):
        self.phase3()

        print self.group_of_next

        # phase 2
