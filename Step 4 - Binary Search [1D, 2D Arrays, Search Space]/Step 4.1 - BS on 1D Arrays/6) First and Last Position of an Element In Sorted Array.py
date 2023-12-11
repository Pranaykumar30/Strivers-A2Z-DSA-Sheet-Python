#https://www.codingninjas.com/studio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def firstAndLastPosition(arr, n, k):
    first, last = -1, -1
    left, right = 0, n - 1

    # Finding first occurrence
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == k:
            first = mid
            right = mid - 1
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    # Finding last occurrence
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == k:
            last = mid
            left = mid + 1
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return first, last