#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0

    for b in range(x):
        try:
            if type(my_list[b]) is int and printed != x:
                print('{:d}'.format(my_list[b]), end='')
                printed += 1
        except TypeError:
            continue
    print()
    return printed
