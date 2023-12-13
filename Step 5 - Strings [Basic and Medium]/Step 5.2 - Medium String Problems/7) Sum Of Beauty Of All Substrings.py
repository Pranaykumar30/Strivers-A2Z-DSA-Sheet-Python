#https://www.codingninjas.com/studio/problems/sum-of-beauty-of-all-substrings_8143656?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def sumOfBeauty(s : str) -> int:
    ans = 0

    for i in range(len(s)):
        mp = {}
        mini = 1
        maxi = 1

        for j in range(i, len(s)):
            if s[j] in mp:
                mp[s[j]] += 1
            else:
                mp[s[j]] = 1

            maxi = max(maxi, mp[s[j]])
            mini = maxi

            for val in mp.values():
                mini = min(mini, val)

            ans += maxi - mini

    return ans