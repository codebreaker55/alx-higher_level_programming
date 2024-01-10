#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda sub_mtrx: list(map(lambda n: n ** 2, sub_mtrx)), matrix))
