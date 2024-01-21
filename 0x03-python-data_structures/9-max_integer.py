#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_int = max(my_list)
    for w in my_list:
        if w > max_int:
            max_int = w

    return max_int
