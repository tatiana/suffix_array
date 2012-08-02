

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
