#https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    max_element = arr[0]
    for i in range(1, n):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element