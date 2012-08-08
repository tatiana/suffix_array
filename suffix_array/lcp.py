from math import log


def lcp_with_substring(text, suffix_array, substring, l, r, llcp, rlcp, M):
    """
    Important: M has to be an index of the binary search path
    """
    if l >= r:
        if llcp[M] == l:
            lcp = l + longest_common_prefix_by_index(\
                text, suffix_array[M] + l, substring, l)
        elif llcp[M] > l:
            lcp = l
        else:
            lcp = llcp[M]
    else:
        if rlcp[M] == r:
            lcp = r + longest_common_prefix_by_index(\
                text, suffix_array[M] + r, substring, r)
        elif rlcp[M] > r:
            lcp = r
        else:
            lcp = rlcp[M]
    return lcp


def lcp_search(text, suffix_array, substring, llcp, rlcp):
    substring_size = len(substring)
    n = len(text)
    L = 0
    R = n - 1
    l = longest_common_prefix_by_index(text, suffix_array[L], substring, 0)
    r = longest_common_prefix_by_index(text, suffix_array[R], substring, 0)
    while (R - L) > 0:
        M = (L + R) / 2
        if (M == L) or (M == R):
            break
        m = lcp_with_substring(text, suffix_array,
            substring, l, r, llcp, rlcp, M)

        if (m == substring_size):
            return suffix_array[M]
        elif (text[suffix_array[M] + m] > substring[m]):
            R = M
            r = m
        else:
            L = M
            l = m
    return -1


def simple_lcp_search(text, suffix_array, substring):

    n = len(text)
    lm, m, rm = compute_binary_search_path(n)
    rlcp = compute_xlcp(rm, m, suffix_array, text)
    llcp = compute_xlcp(lm, m, suffix_array, text)
    return lcp_search(text, suffix_array, substring, llcp, rlcp)


def longest_common_prefix(string1, string2):
    return longest_common_prefix_by_index(string1, 0, string2, 0)


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


def compute_binary_search_path(n):

    lm = [None] * (n)
    rm = [None] * (n)
    m = [None] * (n)

    l_index = 0
    r_index = n - 1

    previous_layer = [(l_index, r_index)]
    tree_level = int(log(n, 2))
    while tree_level > 0:
        current_layer = []
        for (l_index, r_index) in previous_layer:
            m_index = (l_index + r_index) / 2
            if m[m_index] is None:
                m[m_index] = m_index
                rm[m_index] = r_index
                lm[m_index] = l_index
            current_layer.append((l_index, m_index))
            current_layer.append((m_index, r_index))
        previous_layer = current_layer
        tree_level -= 1

    for (l_index, r_index) in current_layer:
        m_index = (l_index + r_index) / 2
        if m[m_index] is None:
            m[m_index] = m_index
            rm[m_index] = r_index
            lm[m_index] = l_index

    return lm[1:n-1], m[1:n-1], rm[1:n-1]


def compute_xlcp(xm, m, suffix_array, text):
    "Used to compute LLCP and RLCP arrays"
    xlcp_array = [None] * len(text)
    i = 0
    for (pos1, pos2) in zip(xm, m):
        i += 1
        lcp = longest_common_prefix_by_index(text, suffix_array[pos1], text, suffix_array[pos2])
        xlcp_array[pos2] = lcp
    return xlcp_array
