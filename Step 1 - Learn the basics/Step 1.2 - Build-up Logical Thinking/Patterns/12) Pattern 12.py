#https://www.codingninjas.com/studio/problems/number-crown_6581894?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def numberCrown(n: int) -> None:
    for i in range(1, n + 1):
            # Number Pattern
            for j in range(1, i + 1):
                print(j, end=" ")
            
            # Space Pattern
            for j in range(1, 2 * (n - i) + 1):
                print(" ", end=" ")
            
            # Number Pattern
            for j in range(i, 0, -1):
                print(j, end=" ")
            
            print()