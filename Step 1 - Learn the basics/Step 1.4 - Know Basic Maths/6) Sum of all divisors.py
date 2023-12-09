#https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def sumOfAllDivisors(n: int) -> int:
    ans = 0
    for i in range(1, n+1):
        ans += i*(n//i)
    return ans
