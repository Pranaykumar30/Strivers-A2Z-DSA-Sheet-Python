#https://www.codingninjas.com/studio/problems/merge-all-overlapping-intervals_6783452?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def mergeOverlappingIntervals(arr : List[List[int]]) -> List[List[int]]:
    if not arr or len(arr) == 1:
        return arr

    arr.sort(key=lambda x: x[0])  # Sort intervals based on the start point
    merged = [arr[0]]

    for start, end in arr[1:]:
        if start <= merged[-1][1]:  # Overlapping interval
            merged[-1][1] = max(merged[-1][1], end)  # Update end point if needed
        else:
            merged.append([start, end])  # Non-overlapping, add new interval

    return merged