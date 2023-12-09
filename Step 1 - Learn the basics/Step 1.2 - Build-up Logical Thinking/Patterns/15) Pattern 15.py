#https://www.codingninjas.com/studio/problems/reverse-letter-triangle_6581906?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def nLetterTriangle(n: int):
    for i in range(n, 0, -1):
            for j in range(ord('A'), ord('A') + i):
                print(chr(j), end='')
            print()
