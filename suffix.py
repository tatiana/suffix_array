class SuffixArray(object):
    def __init__(self, text):
        self._index = 1

        self.text = "%s$" % text
        self.temp_array = []
        self.group = []
        self.group_dict = {}
        self.pending = {}
        self.group_of_next = []

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
        for index in group_indexes:
            items = self.group_dict[index]
            n_items = len(items)
            last_item_index += n_items

            index_in_pending = len(self.group)
            if n_items == 1:
                self.group_dict.pop(index)
            else:
                self.pending[index_in_pending] = n_items

            for i in items:
                self.group.append(last_item_index - 1)

            self.temp_array += items


    def process(self):
        #self.phase3()

        print self.group_of_next

        # phase 2
