#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    """
    function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return ([])

    tr = [[1]]
    while len(tr) != n:
        last_r = tr[-1]
        temp = [1]
        for num in range(len(last_r) - 1):
            temp.append(last_r[num] + last_r[num + 1])
        temp.append(1)
        tr.append(temp)
    return tr
