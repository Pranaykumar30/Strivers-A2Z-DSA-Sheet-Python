#https://www.codingninjas.com/studio/problems/find-peak-element_1081482?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def findPeakElement(arr: [int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if the element to the right is greater
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left