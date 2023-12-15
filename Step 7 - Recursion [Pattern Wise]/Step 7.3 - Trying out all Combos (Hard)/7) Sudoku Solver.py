#https://www.codingninjas.com/studio/problems/sudoku-solver_8416969?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def sudokuSolver(board: List[List[int]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if sudokuSolver(board):
                            return True
                        board[i][j] = 0
                return False
    return True
