#https://www.codingninjas.com/studio/problems/print-subsequences_8416366?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
from typing import List

def generateSubsequences(s:str) -> List[str]:
    N = len(s)
    ans = []

    # Generate all subsequences.
    for i in range(1 << N):
        temp = ""

        # Construct subsequence based on bit representation.
        for j in range(N):
            # Check if j-th bit from left of i is set.
            if i & (1 << (N - 1 - j)):
                # Include character at index j in subsequence.
                temp += s[j]

        # Store generated subsequence in 'ans'.
        ans.append(temp)

    return ans