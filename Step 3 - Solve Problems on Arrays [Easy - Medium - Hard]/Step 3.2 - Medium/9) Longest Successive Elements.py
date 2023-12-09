#https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    if not a:
        return 0

    a.sort()
    max_length = 1
    current_length = 1

    for i in range(1, len(a)):
        if a[i] == a[i - 1] + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length