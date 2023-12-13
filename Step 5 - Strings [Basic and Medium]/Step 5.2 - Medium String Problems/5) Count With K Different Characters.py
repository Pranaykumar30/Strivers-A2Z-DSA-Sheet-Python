#https://www.codingninjas.com/studio/problems/count-with-k-different-characters_1214627?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def most_k_chars(s: str, k: int) -> int:
    mp = {}
    ans = 0
    start = 0
    unique = 0

    for i in range(len(s)):
        if s[i] not in mp or mp[s[i]] == 0:
            unique += 1
        mp[s[i]] = mp.get(s[i], 0) + 1
        
        while unique > k:
            mp[s[start]] -= 1
            if mp[s[start]] == 0:
                unique -= 1
            start += 1
            
        ans += i - start + 1
    
    return ans

def countSubStrings(s: str, k: int) -> int:
    return most_k_chars(s, k) - most_k_chars(s, k - 1)