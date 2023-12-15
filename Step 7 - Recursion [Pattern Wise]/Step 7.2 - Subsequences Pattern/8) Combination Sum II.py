#https://www.codingninjas.com/studio/problems/combination-sum-ii_1112622?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def combinationSum2(arr: List[int], n: int, target: int) -> List[List[int]]:
    def backtrack(start, target, current):
        if target == 0:
            result.append(current[:])
            return

        for i in range(start, n):
            if i > start and arr[i] == arr[i - 1]:
                continue
            if arr[i] > target:
                break
            current.append(arr[i])
            backtrack(i + 1, target - arr[i], current)
            current.pop()

    arr.sort()
    result = []
    backtrack(0, target, [])
    return result
