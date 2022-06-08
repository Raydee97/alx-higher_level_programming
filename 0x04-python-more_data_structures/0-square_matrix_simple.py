#!/usr/bin/python3
"""
computes the square value of all integers of a matrix.

Args: 
    matrix: 2D list to perform operation on

Prints:
    same size and square of all value of a matrix
"""


def square_matrix_simple(matrix=[]):
    square_list = []
    for items in matrix:
        square_list.append(list(map(lambda X: X ** 2, items)))
        print(square_list)
