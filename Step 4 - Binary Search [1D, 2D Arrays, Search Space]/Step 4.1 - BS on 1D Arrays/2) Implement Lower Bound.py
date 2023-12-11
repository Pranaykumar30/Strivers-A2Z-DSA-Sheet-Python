#https://www.codingninjas.com/studio/problems/lower-bound_8165382?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def lowerBound(arr: [int], n: int, x: int) -> int:
    lower = 0
    higher = n - 1
    ans = n

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if arr[mid] >= x:
            ans = mid
            higher = mid - 1
        else:
            lower = mid + 1

    return ans