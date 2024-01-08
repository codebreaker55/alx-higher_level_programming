#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for int_matrix in matrix:
        if len(int_matrix) == 0:
            print()
        else:
            for n in range(len(int_matrix)):
                print(
                        "{:d}".format(int_matrix[n]),
                        end="\n" if n == len(int_matrix) - 1 else " ")
