#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square_list = []
    for items in matrix:
        square_list(list(map(lambda X: X ** 2, items)))
        print(square_list)
