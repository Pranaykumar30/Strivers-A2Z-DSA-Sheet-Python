#https://practice.geeksforgeeks.org/problems/triangle-pattern-1661492263/1
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N + 1):
            print(" " * (N - i) + "*" * (2 * i -1))