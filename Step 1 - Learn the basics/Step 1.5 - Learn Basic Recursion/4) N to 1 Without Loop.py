#https://www.codingninjas.com/studio/problems/n-to-1-without-loop_8357243?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def printNos(x: int) -> List[int]:
    if x <= 0:
        return []
    else:
        nums = [x]
        nums.extend(printNos(x-1))
        return nums
