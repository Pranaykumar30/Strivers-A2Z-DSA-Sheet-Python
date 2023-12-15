#https://www.codingninjas.com/studio/problems/find-x-raised-to-power-n-_626560?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2

    return round(result, 6)from typing import Optional

def createAtoi(s: str) -> int:
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    ans = 0
    check = False  # False indicates positive number

    idx = 0
    while idx < len(s):
        if s[idx] == ' ':
            idx += 1
            continue

        if ans == 0 and s[idx] == '+':
            if idx != 0 and (s[idx - 1] == '+' or s[idx - 1] == '-'):
                return ans
            check = False
            idx += 1
            continue

        if ans == 0 and s[idx] == '-':
            if idx != 0 and (s[idx - 1] == '+' or s[idx - 1] == '-'):
                return ans
            check = True
            idx += 1
            continue

        if not ('0' <= s[idx] <= '9'):
            break

        digit = int(s[idx])
        if ans * 10 + digit > INT_MAX:
            ans = INT_MAX + 5
            break

        ans = ans * 10 + digit
        idx += 1

    if check:
        ans = -ans

    if ans < INT_MIN:
        ans = INT_MIN
    elif ans > INT_MAX:
        ans = INT_MAX

    return ans