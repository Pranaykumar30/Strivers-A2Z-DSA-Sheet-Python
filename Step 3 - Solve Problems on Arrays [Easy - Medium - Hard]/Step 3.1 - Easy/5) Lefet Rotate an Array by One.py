#https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    if n <= 1:
        return arr

    first_element = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]

    arr[n - 1] = first_element
    return arr