#https://www.codingninjas.com/studio/problems/missing-and-repeating-numbers_6828164?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    pXorq = 0
    for i in range(len(a)):
        pXorq ^= (a[i]^(i+1))

    bitDifference = pXorq & (~(pXorq-1))

    p, q = 0, 0

    for i in range(len(a)):
        if (i+1) & bitDifference == 0:
            p ^= (i+1)
        else:
            q ^= (i+1)
        if a[i] & bitDifference == 0:
            p ^= a[i]
        else:
            q ^= a[i]

    count = sum(1 for i in range(len(a)) if a[i] == p)

    if count == 2:
        return [p, q]
    else:
        return [q, p]