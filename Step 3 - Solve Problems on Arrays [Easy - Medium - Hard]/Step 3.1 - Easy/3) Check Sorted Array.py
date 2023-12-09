#https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf\
def isSorted(n: int,  a: [int]) -> int:
    if n <= 1:
        return 1
    for i in range(1, n):
        if a[i - 1] > a[i]:
            return 0
    return 1
