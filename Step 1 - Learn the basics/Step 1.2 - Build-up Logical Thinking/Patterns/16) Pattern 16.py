#https://www.geeksforgeeks.org/problems/triangle-pattern-1662285334/1
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N + 1):
            print(chr(ord('A') + i - 1) * i)