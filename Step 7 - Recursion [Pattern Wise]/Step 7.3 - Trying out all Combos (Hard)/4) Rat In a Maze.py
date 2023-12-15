#https://www.codingninjas.com/studio/problems/rat-in-a-maze-_8842357?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


from typing import List

def solve(i: int, j: int, path: str, matrix: List[List[int]], row: int, column: int, ans: List[str]) -> None:
    # Checking out of bounds conditions.
    if i < 0 or i >= row or j < 0 or j >= column:
        return

    # Avoid recursive calls on blocked or visited numbers.
    if matrix[i][j] == 0:
        return

    # If reached the destination, add the path to the answer list.
    if i == row - 1 and j == column - 1:
        ans.append(path)

    # Mark the current cell as visited (0).
    matrix[i][j] = 0

    # Recursive calls for exploring the next possible moves.
    # Up.
    solve(i - 1, j, path + 'U', matrix, row, column, ans)
    # Down.
    solve(i + 1, j, path + 'D', matrix, row, column, ans)
    # Left.
    solve(i, j - 1, path + 'L', matrix, row, column, ans)
    # Right.
    solve(i, j + 1, path + 'R', matrix, row, column, ans)

    # Restore the current cell to its original state (1).
    matrix[i][j] = 1

def ratMaze(matrix: List[List[int]]) -> List[str]:
    path = ""
    n = len(matrix)
    ans = []
    solve(0, 0, path, matrix, n, n, ans)
    return ans

