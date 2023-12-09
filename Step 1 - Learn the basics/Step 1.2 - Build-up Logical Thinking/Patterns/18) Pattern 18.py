#https://www.codingninjas.com/studio/problems/alpha-triangle_6581429?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
def alphaTriangle(n: int):
    start_char = ord('A') + n - 1
    for i in range(n):
        ch = chr(start_char)
        for j in range(i + 1):
            print(ch, end=" ")
            ch = chr(ord(ch) - 1)
        print()
