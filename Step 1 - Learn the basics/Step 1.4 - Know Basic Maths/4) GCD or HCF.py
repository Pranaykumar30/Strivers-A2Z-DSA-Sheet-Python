#https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def calcGCD(n:int, m: int) -> int:
    ans = 1
    for i in range(1, min(n,m)+1):
        if n%i == 0 and m%i == 0:
            ans=i
    return ans
