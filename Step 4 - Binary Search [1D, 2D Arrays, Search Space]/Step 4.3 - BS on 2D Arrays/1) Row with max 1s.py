"""
    Time Complexity: O(N * M)
    Space Complexity: O(1)

    Where N is the number of rows and M is the number of columns in the given matrix.
"""
#https://www.codingninjas.com/studio/problems/row-of-a-matrix-with-maximum-ones_982768?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:

    #    maxCount stores the maximum number of 1s found till now and ans is the index of that particular row.
    maxCount = 0
    ans = -1

    for i in range(n):
        #    Count for number of ones for the current row.
        curr = 0
        for j in range(m):
            #   Increment count if the value is 1.
            if matrix[i][j] == 1:
                curr += 1

        #    Update curr row and maximum count if the current row has the maximum number of ones.
        if curr > maxCount:
            ans = i
            maxCount = curr

    #    Return the row with maximum number of ones.
    return ans
