#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    list(map(lambda matrix: list(map(lambda x: x*x, matrix)), matrix))
