#https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def sumFirstN(n: int) -> int:
    if n == 0:
        return 0
    else:
        return int((n*(n+1))/2)
