#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elems in matrix:
            b = 1
            length = len(elems)

            for elem in elems:
                if b == length:
                    print('{:d}'.format(elem), end='')
                else:
                    print('{:d}'.format(elem), end=' ')
                b += 1

            print()
