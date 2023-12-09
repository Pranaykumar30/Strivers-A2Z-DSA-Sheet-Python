#https://www.codingninjas.com/studio/problems/increasing-number-triangle_6581893?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def nNumberTriangle(n: int) -> None:
    count = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()