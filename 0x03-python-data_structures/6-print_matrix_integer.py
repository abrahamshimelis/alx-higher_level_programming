#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elements in matrix:
            i = 1
            length = len(elements)
            for element in elements:
                if i == length:
                    print('{:d}'.format(element), end='')
                else:
                    print('{:d}'.format(element), end=' ')
                i +=1
            print()
