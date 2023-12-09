#https://www.codingninjas.com/studio/problems/linear-search_6922070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def linearSearch(n: int, num: int, arr: [int]) -> int:
    for i in range(n):
        if arr[i] == num:
            return i
    return -1