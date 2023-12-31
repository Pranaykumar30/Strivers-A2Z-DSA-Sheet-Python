#https://www.codingninjas.com/studio/problems/kth-missing-element_893215?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def missingK(vec: List[int], n: int, k: int) -> int:
    lower = 0
    higher = n - 1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if vec[mid] - mid - 1 >= k:
            higher = mid - 1
        else:
            lower = mid + 1

    if higher == -1:
        return k
    else:
        return vec[higher] + (k - (vec[higher] - higher - 1))