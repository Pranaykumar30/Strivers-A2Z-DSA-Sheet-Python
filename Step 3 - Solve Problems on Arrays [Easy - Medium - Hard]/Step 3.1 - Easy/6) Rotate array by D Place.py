#https://www.codingninjas.com/studio/problems/rotate-array_1230543?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def rotateArray(arr: list, k: int) -> list:
    if k <= 0 or k == len(arr):
        return arr

    rotated = arr[k:] + arr[:k]
    return rotated