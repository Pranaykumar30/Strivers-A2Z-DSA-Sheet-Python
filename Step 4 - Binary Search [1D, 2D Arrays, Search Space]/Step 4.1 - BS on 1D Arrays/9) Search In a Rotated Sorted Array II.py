#https://www.codingninjas.com/studio/problems/search-in-a-rotated-sorted-array-ii_7449547?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def searchInARotatedSortedArrayII(A : List[int], key : int) -> bool:
    left, right = 0, len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        # If key is found at mid
        if A[mid] == key:
            return True

        # To handle duplicates
        while left < mid and A[left] == A[mid]:
            left += 1

        # Check if the left half is sorted
        if A[left] <= A[mid]:
            if A[left] <= key < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Check if the right half is sorted
        else:
            if A[mid] < key <= A[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False