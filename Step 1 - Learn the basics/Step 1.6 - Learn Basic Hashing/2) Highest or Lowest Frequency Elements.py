#https://www.codingninjas.com/studio/problems/k-most-occurrent-numbers_625382?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List
from collections import Counter

def getFrequencies(v: List[int]) -> List[int]:
    frequency = Counter(v)
    max_freq = max(frequency.values())
    min_freq = min(frequency.values())
    
    maxi = float('-inf')
    mini = float('inf')
    
    for num, freq in frequency.items():
        if freq == max_freq:
            maxi = max(maxi, num)
        if freq == min_freq:
            mini = min(mini, num)
    
    return [maxi, mini]
