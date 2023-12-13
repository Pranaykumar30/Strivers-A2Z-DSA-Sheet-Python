#https://www.codingninjas.com/studio/problems/implement-atoi-function_981270?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import Optional

def createAtoi(s: str) -> int:
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1

    negative = False
    if start < len(s) and s[start] == '-':
        negative = True
        start += 1
    elif start < len(s) and s[start] == '+':
        start += 1

    ans = 0
    count = 0

    while start < len(s):
        if '0' <= s[start] <= '9':
            ans = ans * 10 + int(s[start])
            count += 1
            if count > 10:
                break
        else:
            break
        start += 1

    if negative:
        ans = -ans

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if ans > INT_MAX:
        return INT_MAX
    elif ans < INT_MIN:
        return INT_MIN

    return ans
