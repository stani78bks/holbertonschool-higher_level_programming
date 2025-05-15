#!/usr/bin/python3
"""
This module defines a function to divide all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int/float): divisor

    Returns:
        new matrix with all elements divided by div rounded to 2 decimals

    Raises:
        TypeError: If matrix elements are not int/float or rows not same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/"
                    "floats"
                )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(el / div, 2) for el in row]
        new_matrix.append(new_row)

    return new_matrix
