#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda mtr: list(map(lambda n: n ** 2, mtr)), matrix))
