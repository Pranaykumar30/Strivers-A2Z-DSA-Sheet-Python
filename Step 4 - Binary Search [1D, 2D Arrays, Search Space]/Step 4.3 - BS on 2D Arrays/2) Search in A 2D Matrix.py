#https://www.codingninjas.com/studio/problems/search-in-a-2d-matrix_980531?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def searchMatrix(mat: [[int]], target: int) -> bool:
    rows = len(mat)
    cols = len(mat[0]) if rows > 0 else 0

    lower = 0
    higher = rows * cols - 1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        row = mid // cols
        col = mid % cols

        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            lower = mid + 1
        else:
            higher = mid - 1

    return False