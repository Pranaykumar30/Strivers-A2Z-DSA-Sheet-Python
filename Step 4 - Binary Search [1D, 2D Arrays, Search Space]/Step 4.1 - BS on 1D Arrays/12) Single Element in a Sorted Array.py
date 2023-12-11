#https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def singleNonDuplicate(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Ensure mid is always even-indexed
        if mid % 2 == 1:
            mid -= 1

        # If the element after mid is the same, the single element is on the right
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:  # Single element is on the left side
            right = mid

    return arr[left]
    
