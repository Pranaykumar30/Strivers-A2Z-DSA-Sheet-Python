#https://www.codingninjas.com/studio/problems/ceiling-in-a-sorted-array_1825401?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from os import *
from sys import *
from collections import *
from math import *

def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor, ceil = -1, -1
    left, right = 0, n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if a[mid] == x:
            return a[mid], a[mid]
        elif a[mid] < x:
            floor = a[mid]
            left = mid + 1
        else:
            ceil = a[mid]
            right = mid - 1
    
    return floor, ceil