#https://www.geeksforgeeks.org/problems/triangle-pattern-1662285911/1
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            # Extra spaces
            for j in range(N - i - 1):
                print(" ", end=" ")

            # Alphabet Pattern
            j = 'A'
            for _ in range(i + 1):
                print(j, end="")
                j = chr(ord(j) + 1)

            j = chr(ord(j) - 2)
            for _ in range(i):
                print(j, end="")
                j = chr(ord(j) - 1)

            print()