#https://practice.geeksforgeeks.org/problems/triangle-pattern/1
class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            print("* " * i)