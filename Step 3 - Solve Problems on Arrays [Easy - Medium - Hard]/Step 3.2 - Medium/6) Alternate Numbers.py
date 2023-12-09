#https://www.codingninjas.com/studio/problems/alternate-numbers_6783445?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    positives = [num for num in a if num > 0]
    negatives = [num for num in a if num < 0]

    result = []
    positive_idx, negative_idx = 0, 0

    # Interleave positive and negative elements alternately
    for i in range(len(a)):
        if i % 2 == 0 and positive_idx < len(positives):
            result.append(positives[positive_idx])
            positive_idx += 1
        elif negative_idx < len(negatives):
            result.append(negatives[negative_idx])
            negative_idx += 1

    return result
