#https://www.codingninjas.com/studio/problems/median-of-a-row-wise-sorted-matrix_1115473?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def countNumberLessThan(matrix, value):
    ans = 0
    for row in matrix:
        ans += sum(1 for num in row if num <= value)
    return ans
def median(matrix: [[int]], m: int, n: int) -> int:
    lower = float('inf')
    higher = float('-inf')

    for row in matrix:
        lower = min(lower, row[0])
        higher = max(higher, row[-1])

    check = (m * n) // 2

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if countNumberLessThan(matrix, mid) <= check:
            lower = mid + 1
        else:
            higher = mid - 1
    
    return lower