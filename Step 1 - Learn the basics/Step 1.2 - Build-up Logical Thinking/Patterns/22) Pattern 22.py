#https://www.codingninjas.com/studio/problems/ninja-and-the-number-pattern-i_6581959?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def getNumberPattern(n: int) -> None:
    k = 2 * n - 1

    # Filling up the cells.
    for i in range(k):
        for j in range(k):
            x = abs(i - n + 1)
            y = abs(j - n + 1)
            print(max(x, y) + 1, end="")
        print()