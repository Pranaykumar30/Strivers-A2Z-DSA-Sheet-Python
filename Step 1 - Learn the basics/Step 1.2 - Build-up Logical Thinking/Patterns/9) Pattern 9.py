#https://www.codingninjas.com/studio/problems/star-diamond_6573686?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def nStarDiamond(n: int) -> None:
    gap = n-1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap -= 1
        stars += 2

    gap = 0
    stars = 2 * n - 1
    for i in range(n, 2*n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap += 1
        stars -= 2