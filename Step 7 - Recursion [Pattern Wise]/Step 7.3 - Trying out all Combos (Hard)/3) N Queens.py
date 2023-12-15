#https://www.codingninjas.com/studio/problems/n-queens_696453?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import List

def recurBoard(row: int, n: int, col: List[int], leftDiag: List[bool], rightDiag: List[bool], ans: List[List[int]]) -> None:
    for i in range(n):
        # If the current cell is under attack by any previously placed queen, skip this iteration.
        if leftDiag[row+i] or rightDiag[i-row+n-1] or col[i] != -1:
            continue

        # Place the queen in the current cell and mark the corresponding columns and diagonals as occupied.
        col[i] = row
        leftDiag[row+i] = True
        rightDiag[i-row+n-1] = True

        # If the present row is the last row, save the combination in 'ans'.
        if row+1 == n:
            # Create a temporary list to store the current valid combination.
            temp = []
            for j in range(n):
                for k in range(n):
                    # If there is a queen in cell (j, k), append 1 to temp, otherwise append 0.
                    temp.append(1 if col[k] == j else 0)
            ans.append(temp) # Add the current valid combination to 'ans'.
        else:
            # Check the next row with the current combination of the above rows.
            recurBoard(row+1, n, col, leftDiag, rightDiag, ans)

        # Backtrack: Remove the queen from the current cell and mark the corresponding columns and diagonals as unoccupied.
        col[i] = -1
        leftDiag[row+i] = False
        rightDiag[i-row+n-1] = False


def nQueens(n: int) -> List[List[int]]:
    # Initialize the global variables.
    col = [-1] * n
    leftDiag = [False] * (2*n + 1)
    rightDiag = [False] * (2*n + 1)
    ans = []

    # Solve the N-queens problem recursively.
    recurBoard(0, n, col, leftDiag, rightDiag, ans)

    # Return all valid combinations of queen placements.
    return ans
