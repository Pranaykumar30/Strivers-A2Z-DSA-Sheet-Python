#https://www.codingninjas.com/studio/problems/number-of-inversions_6840276?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def countInversionHelper(a, start, mid, end, count):
    leftIndex, rightIndex = start, mid + 1
    temp = [0] * (end - start + 1)
    tempIndex = 0

    while leftIndex <= mid and rightIndex <= end:
        if a[leftIndex] <= a[rightIndex]:
            temp[tempIndex] = a[leftIndex]
            tempIndex += 1
            leftIndex += 1
        else:
            temp[tempIndex] = a[rightIndex]
            tempIndex += 1
            rightIndex += 1
            count[0] += mid - leftIndex + 1

    while leftIndex <= mid:
        temp[tempIndex] = a[leftIndex]
        tempIndex += 1
        leftIndex += 1
    while rightIndex <= end:
        temp[tempIndex] = a[rightIndex]
        tempIndex += 1
        rightIndex += 1

    tempIndex = 0
    for i in range(start, end + 1):
        a[i] = temp[tempIndex]
        tempIndex += 1

def countInversion(a, start, end, count):
    if start >= end:
        return

    mid = start + (end - start) // 2

    countInversion(a, start, mid, count)
    countInversion(a, mid + 1, end, count)
    countInversionHelper(a, start, mid, end, count)
    return
def numberOfInversions(a : List[int], n : int) -> int:
    count = [0]
    countInversion(a, 0, n - 1, count)

    return count[0]