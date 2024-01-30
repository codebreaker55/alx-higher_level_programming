#!/usr/bin/python3
"""module for multiplying 2 matricies using numpy module"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that is given using numpy module
    Args:
        m_a: is the input first matrix
        m_b: is the input second matrix
    Returns:
        m_a * m_b
    """

    return numpy.matmul(m_a, m_b)
