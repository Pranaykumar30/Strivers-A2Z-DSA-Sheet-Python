#https://www.codingninjas.com/studio/problems/ninja-and-the-zero-s_6581958?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def moveZeros(n: int,  a: [int]) -> [int]:
    non_zero_index = 0
    for i in range(n):
        if a[i] != 0:
            a[non_zero_index] = a[i]
            non_zero_index +=1
    while non_zero_index < n:
        a[non_zero_index] = 0
        non_zero_index+=1
    return a
