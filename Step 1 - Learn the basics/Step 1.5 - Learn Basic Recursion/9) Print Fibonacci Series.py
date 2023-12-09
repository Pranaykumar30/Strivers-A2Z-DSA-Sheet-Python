#https://www.codingninjas.com/studio/problems/print-fibonacci-series_7421617?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    fibonacci =[0, 1]
    for i in range(2, n):
        next_num = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(next_num)
    return fibonacci[:n]
