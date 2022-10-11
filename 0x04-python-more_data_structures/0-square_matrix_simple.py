#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    if len(matrix) > 0:
        for i in matrix:
            newMatrix.append(list(map(lambda x: x**2, i)))
    return newMatrix
