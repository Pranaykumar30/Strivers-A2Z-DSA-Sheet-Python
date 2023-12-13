#https://www.codingninjas.com/studio/problems/longest-common-prefix_628874?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def commonPrefix(arr: List[str], n: int) -> str:
    ans = ""

    for i in range(len(arr[0])):
        ch = arr[0][i]
        check = True

        for j in range(1, len(arr)):
            if i < len(arr[j]) and arr[j][i] != ch:
                check = False
                break

        if check:
            ans += ch
        else:
            break

    if ans:
        return ans
    else:
        return "-1"