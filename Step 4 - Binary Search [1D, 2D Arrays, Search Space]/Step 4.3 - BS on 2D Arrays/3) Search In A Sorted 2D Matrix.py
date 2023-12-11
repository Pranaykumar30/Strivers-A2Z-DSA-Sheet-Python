#https://www.codingninjas.com/studio/problems/search-in-a-sorted-2d-matrix_6917532?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def searchElement(matrix : List[List[int]], target : int) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return 0