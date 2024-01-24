#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dictionary = sorted(a_dictionary.items())

    for x, y in sort_dictionary:
        print('{0}: {1}'.format(x, y))
