#https://www.codingninjas.com/studio/problems/check-armstrong_589?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from os import *
from sys import *
from collections import *
from math import *
def amstrong(n):
    s = str(n)
    n_digits = len(s)
    sum_of_cubes = 0
    for digit in s :
        sum_of_cubes += int(digit) ** n_digits
    return sum_of_cubes == n
n = int(input())
if amstrong(n):
    print("true")
else:
    print("false")
