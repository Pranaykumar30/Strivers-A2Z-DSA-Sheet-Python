#https://www.codingninjas.com/studio/problems/spiral-matrix_6922069?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def spiralMatrix(matrix : List[List[int]]) -> List[int]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    direction = 0
    result = []

    while top <= bottom and left <= right:
        if direction == 0:  # Move from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        elif direction == 1:  # Move from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        elif direction == 2:  # Move from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        elif direction == 3:  # Move from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4  # Update direction for the next traversal

    return result