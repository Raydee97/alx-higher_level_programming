#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    list(map(lambda matrix: list(map(lambda x: x**2, range(matrix))), matrix))
