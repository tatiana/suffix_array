

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

# def suffix_binary_search(text, suffix_array, substring):
#     begin = 0
#     end = len(text)
#     substring_size = len(substring)

#     while begin < end:
#         half = (begin + end) / 2
#         half_value = text[half: half + substring_size]
#         if half_value < substring:
#             begin = half + 1
#         elif half_value > substring:
#             end = half
#         else:
#             return half
#     return -1
