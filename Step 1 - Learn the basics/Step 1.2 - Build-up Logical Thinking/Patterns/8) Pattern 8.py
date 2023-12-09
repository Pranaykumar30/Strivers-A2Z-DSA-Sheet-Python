#https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N, 0, -1):
            print(" " * (N - i) + "*" * (2* i - 1))