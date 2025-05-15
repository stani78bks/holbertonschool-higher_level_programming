#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide
        div (int/float): The divisor

    Returns:
        new matrix with all elements divided by div rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats
                   Or if each row of the matrix is not the same size
                   Or if div is not a number
        ZeroDivisionError: If div is zero

    Examples:
        >>> matrix_divided([[1, 2], [3, 4]], 2)
        [[0.5, 1.0], [1.5, 2.0]]

        >>> matrix_divided([[6.6, 3.3], [9.9, 12.3]], 3)
        [[2.2, 1.1], [3.3, 4.1]]

        >>> matrix_divided([[1, 2], [3]], 2)
        Traceback (most recent call last):
            ...
        TypeError: Each row of the matrix must have the same size

        >>> matrix_divided([[1, 2], ['a', 4]], 2)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided([[1, 2], [3, 4]], "hi")
        Traceback (most recent call last):
            ...
        TypeError: div must be a number

        >>> matrix_divided([[1, 2], [3, 4]], 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        return []

    row_length = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
