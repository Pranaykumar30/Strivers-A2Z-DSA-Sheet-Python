#https://www.codingninjas.com/studio/problems/subarray-with-maximum-product_6890008?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def subarrayWithMaxProduct(arr : List[int]) -> int:
    prefix = 1
    suffix = 1
    maxi = float('-inf')

    for i in range(len(arr)):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= arr[i]
        suffix *= arr[len(arr) - i - 1]

        maxi = max(maxi, prefix, suffix)

    return maxi