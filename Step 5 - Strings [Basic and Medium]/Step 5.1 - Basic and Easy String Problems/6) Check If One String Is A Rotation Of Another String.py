#https://www.codingninjas.com/studio/problems/check-if-one-string-is-a-rotation-of-another-string_1115683?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def isCyclicRotation(p: str, q: str) -> int:
    if len(p) != len(q):
     return 0
    
    p = p + p
    if q in p:
        return 1
    else:
        return 0