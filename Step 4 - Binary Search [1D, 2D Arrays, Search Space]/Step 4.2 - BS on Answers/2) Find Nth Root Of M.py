#https://www.codingninjas.com/studio/problems/nth-root-of-m_1062679?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def NthRoot(n: int, m: int) -> int:
    if m == 0:
        return 0

    # Binary search for the approximate root value
    low, high = 0, m
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if mid ** n == m:
            return mid
        elif mid ** n < m:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans if ans ** n == m else -1
