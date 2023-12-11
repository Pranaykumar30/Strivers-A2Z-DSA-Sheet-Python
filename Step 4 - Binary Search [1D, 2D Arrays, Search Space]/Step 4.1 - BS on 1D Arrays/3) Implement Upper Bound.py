#https://www.codingninjas.com/studio/problems/implement-upper-bound_8165383?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def upperBound(arr: [int], x: int, n: int) -> int:
    lower = 0
    higher = n - 1
    ans = n

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if arr[mid] > x:
            ans = mid
            higher = mid - 1
        else:
            lower = mid + 1

    return ans