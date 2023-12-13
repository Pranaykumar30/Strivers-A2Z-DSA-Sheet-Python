#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        currCount = 0
        for ele in s:
            if ele == '(':
                currCount += 1
            elif ele == ')':
                currCount -= 1
            ans = max(ans, currCount)
        return ans