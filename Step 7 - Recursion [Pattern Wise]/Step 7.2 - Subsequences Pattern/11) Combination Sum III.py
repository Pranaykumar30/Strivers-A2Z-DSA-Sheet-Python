#https://www.codingninjas.com/studio/problems/combination-sum-iii_5038357?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def combinationSum(k: int, n: int) -> List[List[int]]:
    def backtrack(start, target, path):
        if target == 0 and len(path) == k:
            result.append(path[:])
            return

        for i in range(start, 10):
            if i > target:
                break
            path.append(i)
            backtrack(i + 1, target - i, path)
            path.pop()

    result = []
    backtrack(1, n, [])
    return result
