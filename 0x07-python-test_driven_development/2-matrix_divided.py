#!/usr/bin/python3
"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix
    Args:
        matrix: List of lists containing int or float
        div: is the number to divide matrix by
    Raises:
        TypeError: If matrix is not list of lists containing int or float
        TypeError: If sublists are not all same size
        TypeError: If div is not int or float
        ZeroDivisionError: If div is zero
    Returns:
        List of lists representing divided matrix
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(n / div, 2) for n in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
