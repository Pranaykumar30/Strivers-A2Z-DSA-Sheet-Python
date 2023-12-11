#https://www.codingninjas.com/studio/problems/rotated-array_1093219?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def findMin(arr: [int]):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if the mid element is greater than the rightmost element
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]