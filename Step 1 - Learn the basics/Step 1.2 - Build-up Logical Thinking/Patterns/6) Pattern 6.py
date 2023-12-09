#https://practice.geeksforgeeks.org/problems/triangle-number-1661489840/1
class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()