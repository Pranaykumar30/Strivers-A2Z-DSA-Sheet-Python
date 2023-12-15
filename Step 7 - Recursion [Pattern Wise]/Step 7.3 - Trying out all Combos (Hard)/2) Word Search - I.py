#https://www.codingninjas.com/studio/problems/word-search---l_892986?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import List

def dfs(i: int, j: int, n: int, m: int, board: List[List[str]], word: str, k: int) -> bool:
    # Check if the word has been found.
    if k == len(word):
        return True

    # Check if the current position is out of bounds or the cell is visited or doesn't match the current letter.
    elif i < 0 or i == n or j < 0 or j == m or board[i][j] == '#' or board[i][j] != word[k]:
        return False
    else:
        # Store the value of the current cell.
        temp = board[i][j]

        # Mark the current cell as visited.
        board[i][j] = '#'

        # Recursively call dfs for the neighboring cells.
        op1 = dfs(i + 1, j, n, m, board, word, k + 1)
        op2 = dfs(i, j + 1, n, m, board, word, k + 1)
        op3 = dfs(i - 1, j, n, m, board, word, k + 1)
        op4 = dfs(i, j - 1, n, m, board, word, k + 1)

        # Restore the original value of the current cell.
        board[i][j] = temp

        # Return True if any of the neighboring cells found the word.
        return op1 or op2 or op3 or op4


def present(board: List[List[str]], word: str, n: int, m: int) -> bool:
    # Number of rows and columns in the board.
    n, m = len(board), len(board[0])

    # Checking for each cell on the board.
    for i in range(n):
        for j in range(m):
            # If the first letter matches.
            if board[i][j] == word[0]:
                # Call dfs function to check if the word can be formed starting from the current cell.
                if dfs(i, j, n, m, board, word, 0):
                    return True

    # Word not found on the board.
    return False

