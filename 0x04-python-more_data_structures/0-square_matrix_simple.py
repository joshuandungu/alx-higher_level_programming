#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = []

    if len(matrix) > 0:
        for elems in matrix[:]:
            _matrix.append(list(map(lambda x: x ** 2, elems)))

    return _matrix
