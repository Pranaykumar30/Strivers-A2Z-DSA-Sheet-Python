#https://www.codingninjas.com/studio/problems/ninja-and-the-star-pattern-i_6581920?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def getStarPattern(n: int) -> None:
    if n == 1:
        print("*")
        return

    print("*" * n)
    for i in range(n - 2):
        print("*" + " " * (n - 2) + "*")
    print("*" * n)