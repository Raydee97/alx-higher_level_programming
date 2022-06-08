#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    list(map(lambda newmatrix: list(map(lambda x: x*x, newmatrix)), matrix))
