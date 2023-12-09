#https://www.codingninjas.com/studio/problems/merge-two-sorted-arrays-without-extra-space_6898839?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    maxValue = 10**9 + 1

    ansIndexA, ansIndexB = 0, 0
    indexA, indexB = 0, 0

    while indexA < len(a) and indexB < len(b):
        valueA = a[indexA] // maxValue if a[indexA] > maxValue else a[indexA]
        valueB = b[indexB] // maxValue if b[indexB] > maxValue else b[indexB]

        if valueA < valueB:
            if ansIndexA < len(a):
                a[ansIndexA] = a[ansIndexA] * maxValue + valueA
                ansIndexA += 1
            else:
                b[ansIndexB] = b[ansIndexB] * maxValue + valueA
                ansIndexB += 1

            indexA += 1
        else:
            if ansIndexA < len(a):
                a[ansIndexA] = a[ansIndexA] * maxValue + valueB
                ansIndexA += 1
            else:
                b[ansIndexB] = b[ansIndexB] * maxValue + valueB
                ansIndexB += 1

            indexB += 1

    while indexA < len(a):
        valueA = a[indexA] // maxValue if a[indexA] > maxValue else a[indexA]
        if ansIndexA < len(a):
            a[ansIndexA] = a[ansIndexA] * maxValue + valueA
            ansIndexA += 1
        else:
            b[ansIndexB] = b[ansIndexB] * maxValue + valueA
            ansIndexB += 1

        indexA += 1

    while indexB < len(b):
        valueB = b[indexB] // maxValue if b[indexB] > maxValue else b[indexB]
        if ansIndexA < len(a):
            a[ansIndexA] = a[ansIndexA] * maxValue + valueB
            ansIndexA += 1
        else:
            b[ansIndexB] = b[ansIndexB] * maxValue + valueB
            ansIndexB += 1

        indexB += 1

    for i in range(len(a)):
        a[i] = a[i] % maxValue

    for i in range(len(b)):
        b[i] = b[i] % maxValue