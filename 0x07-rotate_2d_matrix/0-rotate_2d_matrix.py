#!/usr/bin/python3
"""
Solves the rotate 2D problem.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
