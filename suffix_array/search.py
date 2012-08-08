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


def compare_strings(string1, string2):
    i = 0
    while True:
        try:
            if string1[i] > string2[i]:
                return 1
            elif string1[i] < string2[i]:
                return -1
        except IndexError:
            break
        i += 1
    return 0


def suffix_binary_search(text, suffix_array, substring):
    begin = 0
    end = len(suffix_array)
    substring_size = len(substring)

    while begin < end:
        half = (begin + end) / 2
        index = suffix_array[half]
        half_value = text[index: index + substring_size]
        #if half_value < substring:
        if compare_strings(half_value, substring) == -1:
            begin = half + 1
        #elif half_value > substring:
        elif compare_strings(half_value, substring) == 1:
            end = half
        else:
            return index
    return -1
