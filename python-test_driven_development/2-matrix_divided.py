#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.
    Args:
        matrix (list of lists of int/float): Matrix to divide.
        div (int or float): Divisor.
    Returns:
        new matrix with all elements divided.
    Raises:
        TypeError: If matrix is not a matrix of ints/floats,
                   or if rows are not all the same size,
                   or if div is not a number.
        ZeroDivisionError: If div == 0.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
