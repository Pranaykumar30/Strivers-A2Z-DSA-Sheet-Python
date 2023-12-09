#https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    frequency = [0] * n
    for edge in edges:
        if edge - 1 < n:
            frequency [edge - 1] += 1
    return frequency
