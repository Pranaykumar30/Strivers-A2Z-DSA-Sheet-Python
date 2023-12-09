#https://www.codingninjas.com/studio/problems/switch-case-statement_8357244?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    area = 0.0
    if (ch == 1):
        area = math.pi*a[0]*a[0]
    if (ch == 2):
        area = a[0]*a[1]
    return "{:.5f}".format(area)