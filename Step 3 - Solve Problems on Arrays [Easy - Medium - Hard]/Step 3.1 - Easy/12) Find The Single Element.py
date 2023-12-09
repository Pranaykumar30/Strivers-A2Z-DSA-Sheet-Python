#https://www.codingninjas.com/studio/problems/find-the-single-element_6680465?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def getSingleElement(arr : List[int]) -> int:
    result = 0
    for num in arr:
        result ^= num
    return result