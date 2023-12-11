#https://www.codingninjas.com/studio/problems/rotation_7449070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def findKRotation(arr : [int]) -> int:
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        if arr[left] <= arr[right]:  # Case 1: The array is already sorted
            return left

        mid = (left + right) // 2
        prev = (mid + n - 1) % n
        next_ = (mid + 1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next_]:  # Case 2: Found the minimum element
            return mid

        if arr[mid] >= arr[left]:  # Check if the left side is sorted, if so, the minimum is on the right
            left = mid + 1
        else:  # Otherwise, search the unsorted side
            right = mid - 1

    return -1 