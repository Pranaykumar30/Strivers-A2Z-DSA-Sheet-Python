#https://www.codingninjas.com/studio/problems/sorting-characters-by-frequency_1263699?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from collections import Counter
import heapq

def sortByFrequency(n: int, s: str) -> str:
    char_freq = Counter(s)
    pq = [(-freq, char) for char, freq in char_freq.items()]
    heapq.heapify(pq)

    ans = ''
    while pq:
        freq, char = heapq.heappop(pq)
        ans += char * (-freq)

    return ans