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


def longest_common_prefix(string1, string2):
    return longest_common_prefix_by_index(string1, 0, string2, 0)
    # i = 0
    # while True:
    #     try:
    #         if string1[i] != string2[i]:
    #             break
    #     except IndexError:
    #         break
    #     i += 1
    # return i

def longest_common_prefix_by_index(text1, pos1, text2, pos2):
    i = 0
    while True:
        try:
            if text1[pos1 + i] != text2[pos2 + i]:
                break
        except IndexError:
            break
        i += 1
    return i

def compute_lcp_array(text, suffix_array):
    assert len(text) == len(suffix_array)
    lcp = [0] * len(suffix_array)
    n = len(suffix_array)
    for i in xrange(1, n):
        index1 = suffix_array[i - 1]
        index2 = suffix_array[i]
        lcp[i] = longest_common_prefix(text[index1:], text[index2:])

    return lcp

@profile
def lcp_search(text, suffix_array, substring):

    P = substring

    l_index = 0
    l_text_index = suffix_array[l_index]
    L = text[l_text_index:]
    #l = longest_common_prefix(L, P)
    l = longest_common_prefix_by_index(text, l_text_index, substring, 0)

    r_index = len(suffix_array) - 1
    r_text_index = suffix_array[r_index]
    R = text[r_text_index:]
    #r = longest_common_prefix(R, P)
    r = longest_common_prefix_by_index(text, r_text_index, substring, 0)

    m_index = -1

    while l_index < r_index:

        new_m_index = (l_index + r_index) / 2
        if m_index == new_m_index:
            return -1
        m_index = new_m_index
        m_text_index = suffix_array[m_index]
        M = text[m_text_index:]
        # case 1
        if l == r:
            lcp = longest_common_prefix_by_index(substring, l, text, m_text_index + l)
            #lcp = longest_common_prefix(P[l:], M[l:])

            j = lcp + l  # 0 first mismatch

            if lcp == (len(P) - l):
                return suffix_array[m_index]

            mismatch_index = l + lcp
            if M[mismatch_index] < P[mismatch_index]:  # lower half
                L = M
                l_index = m_index
                l_text_index = m_text_index
                l = j
            else:  # P[mismatch_index] < M[mismatch_index]:  # upper half
                R = M
                r_index = m_index
                r_text_index = m_text_index
                r = j

        # case 2
        elif l > r:
            #lcp = longest_common_prefix(L, M)
            lcp = longest_common_prefix_by_index(text, l_text_index, text, m_text_index)

            if lcp < l:  # go left
                R = M
                r_index = m_index
                r_text_index = m_text_index
                #r = longest_common_prefix(R, P)
                r = longest_common_prefix_by_index(text, r_text_index, substring, 0)
            elif lcp > l:  # go right
                L = M
                l_index = m_index
                l_text_index = m_text_index
                #l = longest_common_prefix(L, P)
                l = longest_common_prefix_by_index(text, l_text_index, substring, 0)
            else:
                # TODO: REFACTOR!!!  argh
                #lcp = longest_common_prefix(P[l:], M[l:])
                lcp = longest_common_prefix_by_index(substring, l, text, m_text_index + l)

                j = lcp + l  # 0 first mismatch

                if lcp == (len(P) - l):
                    return suffix_array[m_index]

                mismatch_index = l + lcp
                if M[mismatch_index] > P[mismatch_index]:  # lower half
                    R = M
                    r_index = m_index
                    r_text_index = m_text_index
                    r = j

                else:  # P[mismatch_index] < M[mismatch_index]:  # upper half
                    L = M
                    l_index = m_index
                    l_text_index = m_text_index
                    l = j

        else:  # elif r > l:
            #lcp = longest_common_prefix(R, M)
            lcp = longest_common_prefix_by_index(text, r_text_index, text, m_text_index)

            if lcp < r:  # go right
                L = M
                l_index = m_index
                l_text_index = m_text_index
                #l = longest_common_prefix(L, P)
                l = longest_common_prefix_by_index(text, l_text_index, substring, 0)
            elif lcp > r:  # go left
                R = M
                r_index = m_index
                r_text_index = m_text_index
                #r = longest_common_prefix(R, P)
                r = longest_common_prefix_by_index(text, r_text_index, substring, 0)
            else:
                # TODO: refactor!
                #lcp = longest_common_prefix(P[r:], M[r:])
                lcp = longest_common_prefix_by_index(substring, r, text, m_text_index + r)

                j = lcp + r  # 0 first mismatch

                if lcp == (len(P) - r):
                    return suffix_array[m_index]

                mismatch_index = r + lcp
                if M[mismatch_index] > P[mismatch_index]:  # lower half
                    R = M
                    r_index = m_index
                    r_text_index = m_text_index
                    r = j
                else:  # elif P[mismatch_index] < M[mismatch_index]:  # upper half
                    L = M
                    l_index = m_index
                    l_text_index = m_text_index
                    l = j

        if l == len(P):
            return suffix_array[l_index]
        elif r == len(P):
            return suffix_array[r_index]

    return -1
