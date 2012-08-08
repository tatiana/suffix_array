

suffix_array = []
text = ""
longest_common_prefix = lambda a, b: None


###
# 0 - 11  $   0
# 1 - 10  a$  0
# 2 - 7   abra$   1
# 3 - 0   abracadabra$    4
# 4 - 3   acadabra$   1
# 5 - 5   adabra$ 1
# 6 - 8   bra$    0
# 7 - 1   bracadabra$ 3
# 8 - 4   cadabra$    0
# 9 - 6   dabra$  0
# 10 - 9  ra$ 0
# 11 - 2   racadabra$  2]

