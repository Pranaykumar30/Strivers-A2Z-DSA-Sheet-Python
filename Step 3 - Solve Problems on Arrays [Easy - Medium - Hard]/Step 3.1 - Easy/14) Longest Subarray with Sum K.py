#https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_5713505?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    sum_map = {0: -1}  # Initialize with sum 0 at index -1
    max_length = 0
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum - k in sum_map:
            max_length = max(max_length, i - sum_map[current_sum - k])

        if current_sum not in sum_map:
            sum_map[current_sum] = i

    return max_length