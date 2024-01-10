#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda smtrx: list(map(lambda n: n ** 2, smtrx)), matrix))
