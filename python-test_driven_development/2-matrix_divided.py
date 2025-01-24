#!/usr/bin/python3
"""
This module contains the matrix_divided function.

The matrix_divided function takes a matrix and a divisor,
and returns a new matrix with each element divided by the divisor.
"""


def matrix_divided(matrix, div):
    '''
    Divise tous les éléments de la matrice par div et renvoie une nouvelle matrice.
    
    Parameters:
    matrix : (list of lists of int/float) - La matrice d'origine, où chaque élément est une liste contenant des 
    nombres entiers ou 
    flottants.
    div: (int, float) - Le diviseur par lequel chaque élément de la matrice sera divisé.
    
    retunrs :
    list of lists of float: Une nouvelle matrice avec les valeurs divisées par div et 
    arrondies à deux décimales.
     
    Raises:
        TypeError: Si les éléments de la matrice ne sont pas des
        listes d'entiers ou de flottants, 
        ou si div n'est pas un entier/flottant.
        ZeroDivisionError: Si div est zéro.
    
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 1)
        [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]'''
        
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)of integers/floats")
    if not all(all(isinstance(item, (int, float)) for item in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
