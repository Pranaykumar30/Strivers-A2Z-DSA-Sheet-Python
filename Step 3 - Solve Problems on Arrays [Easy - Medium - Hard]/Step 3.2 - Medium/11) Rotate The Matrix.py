#https://www.codingninjas.com/studio/problems/rotate-the-matrix_6825090?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def rotateMatrix(mat : List[List[int]]):
    if not mat:
        return

    n = len(mat)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Reverse each row to complete the rotation
    for row in mat:
        row.reverse()
        