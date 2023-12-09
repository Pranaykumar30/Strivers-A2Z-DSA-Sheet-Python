#https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def superiorElements(a : List[int]) -> List[int]:
    result = []
    max_element = float('-inf')  # Initialize the maximum element encountered

    # Traverse the array from right to left
    for i in range(len(a) - 1, -1, -1):
        if a[i] > max_element:
            result.append(a[i])  # Add the superior element to the result
            max_element = a[i]   # Update the maximum element encountered

    return sorted(result)