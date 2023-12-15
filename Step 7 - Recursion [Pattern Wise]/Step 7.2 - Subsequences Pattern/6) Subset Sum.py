#https://www.codingninjas.com/studio/problems/subset-sum_630213?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    dp = [False] * (k + 1)
    dp[0] = True

    for num in a:
        for i in range(k, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[k]