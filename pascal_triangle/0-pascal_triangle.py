#!/usr/bin/python3
'''A module for working with pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a lists of integers representing
    the pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triange
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triange[i - 1][j - 1] + triange[i - 1][j])
        triange.append(line)
    return triangle
