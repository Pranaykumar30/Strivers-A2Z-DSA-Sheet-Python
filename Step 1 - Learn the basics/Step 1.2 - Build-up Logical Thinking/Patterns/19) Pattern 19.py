#https://www.codingninjas.com/studio/problems/symmetric-void_6581919?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def symmetry(n: int):
    n = 2*n

    # For loop ‘row’ in range 0 to N-1.
    for row in range(n):
        # For loop ‘col’ in range 0 to N-1.
        for col in range(n):
            # Condition for first half of the rows.
            if (row < n//2 and (col < (n//2 - row) or col >= (n//2 + row))):
                print('*', end=" ")
            # Condition for the second half of the rows.
            if (row >= n//2 and (col <= (row-n//2) or col >= (n-row+n//2-1))):
                print('*', end=" ")
            if (row < n//2 and not (col < (n//2 - row) or col >= (n//2 + row))):
                print(" ", end=" ")
            if (row >= n//2 and not (col <= (row-n//2) or col >= (n-row+n//2-1))):
                print(" ", end=" ")
        print()