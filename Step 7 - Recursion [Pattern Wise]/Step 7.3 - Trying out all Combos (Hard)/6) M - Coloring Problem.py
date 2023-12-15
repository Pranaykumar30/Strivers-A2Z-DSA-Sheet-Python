#https://www.codingninjas.com/studio/problems/m-coloring-problem_981273?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def graphColoring(mat: List[List[int]], m: int) -> str:
    def isSafe(v, color, c):
        for i in range(len(mat)):
            if mat[v][i] == 1 and color[i] == c:
                return False
        return True

    def graphColorUtil(v, color):
        if v == len(mat):
            return True

        for c in range(1, m + 1):
            if isSafe(v, color, c):
                color[v] = c
                if graphColorUtil(v + 1, color):
                    return True
                color[v] = 0

    color = [0] * len(mat)
    if graphColorUtil(0, color):
        return "YES"
    return "NO"
