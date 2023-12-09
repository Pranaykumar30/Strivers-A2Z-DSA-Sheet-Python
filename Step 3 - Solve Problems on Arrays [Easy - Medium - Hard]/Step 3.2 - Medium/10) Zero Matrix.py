#https://www.codingninjas.com/studio/problems/zero-matrix_1171153?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    make0Row0 = False
    for coln in range(m):
        if matrix[0][coln] == 0:
            make0Row0 = True

    make0Coln0 = False
    for row in range(n):
        if matrix[row][0] == 0:
            make0Coln0 = True

    for row in range(1, n):
        for coln in range(1, m):
            if matrix[row][coln] == 0:
                matrix[0][coln] = 0
                matrix[row][0] = 0

    for coln in range(m - 1, 0, -1):
        if matrix[0][coln] == 0:
            for row in range(n):
                matrix[row][coln] = 0

    for row in range(1, n):
        if matrix[row][0] == 0:
            for coln in range(m):
                matrix[row][coln] = 0

    if make0Row0:
        for coln in range(m):
            matrix[0][coln] = 0

    if make0Coln0:
        for row in range(n):
            matrix[row][0] = 0

    return matrix