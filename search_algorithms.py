import math

def linear_search(input_list, val):
    for i in range(len(input_list)):
        if input_list[i] == val:
            return i
    return -1

#input_list must be sorted
def binary_search(input_list, val):
    i, j = 0, len(input_list) - 1
    while i < j:
        m = math.floor((i + j)/2)
        if val > input_list[m]:
            i = m + 1
        else:
            j = m
    if val == input_list[i]:
        return i
    return -1
