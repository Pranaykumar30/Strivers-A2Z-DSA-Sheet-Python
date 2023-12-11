#https://www.codingninjas.com/studio/problems/shttps://www.codingninjas.com/studio/problems/smallest-divisor-with-the-given-limit_1755882?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetufmallest-divisor-with-the-given-limit_1755882?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from os import *
from sys import *
from collections import *
from math import *

def check_threshold(arr, divisor, limit):
    total_sum = 0
    for num in arr:
        total_sum += ceil(num / divisor)
    return total_sum <= limit
def smallestDivisor(arr: [int], limit: int) -> int:
    lower = 1
    higher = max(arr)
    ans = -1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if check_threshold(arr, mid, limit):
            ans = mid
            higher = mid - 1
        else:
            lower = mid + 1

    return ans
    