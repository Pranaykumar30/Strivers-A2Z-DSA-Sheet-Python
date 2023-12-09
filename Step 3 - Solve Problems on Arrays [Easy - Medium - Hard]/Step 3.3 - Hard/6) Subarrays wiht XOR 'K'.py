#https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from collections import defaultdict
def subarraysWithSumK(a: [int], b: int) -> int:
    prefix_xor = defaultdict(int)
    prefix_xor[0] = 1  # To handle the subarrays that start at index 0
    xor_sum = 0
    count = 0

    for num in a:
        xor_sum ^= num
        count += prefix_xor[xor_sum ^ b]
        prefix_xor[xor_sum] += 1

    return count