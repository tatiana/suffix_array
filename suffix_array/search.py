def binary_search(array, value):
    begin = 0
    end = len(array)

    while begin < end:
        half = (begin + end) / 2
        half_value = array[half]
        if half_value < value:
            begin = half + 1
        elif half_value > value:
            end = half
        else:
            return half
    return -1


def substring_binary_search(text, substring):
    begin = 0
    end = len(text)
    substring_size = len(substring)

    while begin < end:
        half = (begin + end) / 2
        half_value = text[half: half + substring_size]
        if half_value < substring:
            begin = half + 1
        elif half_value > substring:
            end = half
        else:
            return half
    return -1


def suffix_binary_search(text, suffix_array, substring):
    begin = 0
    end = len(suffix_array)
    substring_size = len(substring)

    while begin < end:
        half = (begin + end) / 2
        index = suffix_array[half]
        half_value = text[index: index + substring_size]
        if half_value < substring:
            begin = half + 1
        elif half_value > substring:
            end = half
        else:
            return index
    return -1


def longest_common_preffix(string1, string2):
    lcp = string1[:[c[0] == c[1] for c in zip(string1, string2)].index(0)]
    return len(lcp)


# def compute_lcp_array(text, suffix_array):
#     lcp = [None] * len(suffix_array)
#     for i in len(suffix_array):
