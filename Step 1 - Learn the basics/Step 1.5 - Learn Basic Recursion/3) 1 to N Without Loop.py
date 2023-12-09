#https://www.codingninjas.com/studio/problems/print-1-to-n_628290?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def printNos(x: int) -> List[int]:
    if x > 0:
        numbers = printNos(x - 1)
        numbers.append(x)
        return numbers
    else:
        return []
