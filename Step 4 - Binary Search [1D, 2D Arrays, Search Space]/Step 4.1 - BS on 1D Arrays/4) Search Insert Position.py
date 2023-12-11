#https://www.codingninjas.com/studio/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def searchInsert(arr: [int], m: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == m:
            return mid
        elif arr[mid] < m:
            left = mid + 1
        else:
            right = mid - 1

    return left