#https://www.codingninjas.com/studio/problems/rotated-triangle_6573688?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def nStarTriangle(n: int) -> None:
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i)