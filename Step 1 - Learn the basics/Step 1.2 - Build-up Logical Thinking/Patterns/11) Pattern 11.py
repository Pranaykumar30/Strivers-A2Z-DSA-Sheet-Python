#https://www.codingninjas.com/studio/problems/binary-number-triangle_6581890?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def nBinaryTriangle(n: int) -> None:
    for i in range(n):
            for j in range(i, -1, -1):
                if j % 2 == 0:
                    print("1 ", end="")
                else:
                    print("0 ", end="")
            print()