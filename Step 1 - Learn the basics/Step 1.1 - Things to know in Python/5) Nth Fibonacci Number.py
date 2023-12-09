#https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from math import *
from collections import *
from sys import *
from os import *


## Read input as specified in the question.
## Print output as specified in the question.
def Fibonacci(n):
    if n < 0:
      return "not supported"
    elif n == 0:
      return 0
    elif n == 1 or n ==2:
      return 1
    else:
      return Fibonacci(n-1) + Fibonacci(n-2)
n = input()

print(Fibonacci(int(n)))