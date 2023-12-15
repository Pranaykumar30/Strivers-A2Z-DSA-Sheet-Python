#https://www.codingninjas.com/studio/problems/subset-sum_3843086?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from os import *
from sys import *
from collections import *
from math import *

from typing import List

def subsetSum(nums: List[int]) -> List[int]:
    def backtrack(start, path_sum):
        result.append(path_sum)
        for i in range(start, len(nums)):
            backtrack(i + 1, path_sum + nums[i])

    result = []
    backtrack(0, 0)
    return sorted(result)
