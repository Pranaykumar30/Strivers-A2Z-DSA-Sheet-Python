#https://www.codingninjas.com/studio/problems/next-greater-permutation_6929564?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def nextGreaterPermutation(A : List[int]) -> List[int]:
    i = len(A) - 2
    while i >= 0 and A[i] >= A[i + 1]:
        i -= 1

    if i >= 0:
        # Find the next greater element to swap with
        j = len(A) - 1
        while A[j] <= A[i]:
            j -= 1
        A[i], A[j] = A[j], A[i]

    # Reverse the subarray to the right of i
    left, right = i + 1, len(A) - 1
    while left < right:
        A[left], A[right] = A[right], A[left]
        left += 1
        right -= 1

    return A