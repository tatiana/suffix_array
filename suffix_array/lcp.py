from math import log


def compute_binary_search_path(n):

    lm = [None] * (n)
    rm = [None] * (n)
    m = [None] * (n)

    l_index = 0
    r_index = n - 1

    previous_layer = [(l_index, r_index)]
    stack = [(l_index, r_index)]
    tree_level = int(log(n, 2))
    while tree_level > 1:
        current_layer = []
        for (l_index, r_index) in previous_layer:
            m_index = (l_index + r_index) / 2
            current_layer.append((l_index, m_index))
            current_layer.append((m_index, r_index))
        previous_layer = current_layer
        stack += current_layer
        tree_level -= 1

    while stack and (None in m):
        (l_index, r_index) = stack.pop(0)
        m_index = (l_index + r_index) / 2
        m[m_index] = m_index
        rm[m_index] = r_index
        lm[m_index] = l_index

    return lm[1:n-1], m[1:n-1], rm[1:n-1]
