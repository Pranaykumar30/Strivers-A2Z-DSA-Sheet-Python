#https://www.codingninjas.com/studio/problems/subarray-sums-i_1467103?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from os import *
from sys import *
from collections import *
from math import *

def findAllSubarraysWithGivenSum(arr, s):
    count = 0
    sum_freq = {0: 1}  # Initialize a dictionary to store cumulative sum frequencies
    current_sum = 0

    for num in arr:
        current_sum += num
        count += sum_freq.get(current_sum - s, 0)  # Check if (current_sum - s) is in the dictionary
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1  # Update cumulative sum frequency

    return count