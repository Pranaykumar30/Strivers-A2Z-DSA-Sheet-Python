"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
#https://www.codingninjas.com/studio/problems/quick-sort_5844?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List
def partition(arr: List[int], start: int, end: int) -> int:
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if startIndex < endIndex:
        pivotIndex = partition(arr, startIndex, endIndex)
        quickSort(arr, startIndex, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, endIndex)
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    pass