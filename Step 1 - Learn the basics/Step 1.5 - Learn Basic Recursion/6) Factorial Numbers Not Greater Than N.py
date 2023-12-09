#https://www.codingninjas.com/studio/problems/factorial-numbers-not-greater-than-n_8365435?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def factorialNumbers(n: int) -> List[int]:
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num - 1)
    result = []
    i = 1
    while factorial(i) <=n:
        result.append(factorial(i))
        i += 1
    return result
