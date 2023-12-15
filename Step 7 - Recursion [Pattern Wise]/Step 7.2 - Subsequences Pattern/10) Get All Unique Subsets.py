#https://www.codingninjas.com/studio/problems/get-all-unique-subsets_624393?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from math import *
from collections import *
from sys import *
from os import *
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        nums.sort()
        result = []
        backtrack(0, [])
        return result



if __name__ == "__main__":
    n= int (input())
    nums=list(map(int, input().split()))  
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()