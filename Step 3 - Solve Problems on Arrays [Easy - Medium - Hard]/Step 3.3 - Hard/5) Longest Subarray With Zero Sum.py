#https://www.codingninjas.com/studio/problems/longest-subarray-with-zero-sum_6783450?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    sum_indices = {}
    max_len = 0
    curr_sum = 0
    n = len(arr)

    for i in range(n):
        curr_sum += arr[i]
        if arr[i] == 0 and max_len == 0:
            max_len = 1
        if curr_sum == 0:
            max_len = i + 1
        if curr_sum in sum_indices:
            max_len = max(max_len, i - sum_indices[curr_sum])
        else:
            sum_indices[curr_sum] = i

    return max_len