#https://www.codingninjas.com/studio/problems/occurrence-of-x-in-a-sorted-array_630456?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def count(arr: [int], n: int, x: int) -> int:
    start = arr.index(x) if x in arr else -1
    
    if start == -1:
        return 0
    
    end = arr[start:].count(x) + start
    return end - start