#https://www.codingninjas.com/studio/problems/more-subsequence_8842355?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def countDistinctSubsequences(s):
    mod = 10 ** 9 + 7
    last = {}
    dp = [0] * (len(s) + 1)
    dp[0] = 1

    for i, char in enumerate(s, 1):
        dp[i] = (2 * dp[i - 1]) % mod

        if char in last:
            dp[i] = (dp[i] - dp[last[char] - 1] + mod) % mod

        last[char] = i

    return dp[-1] - 1
def moreSubsequence(n: int, m: int, a: str, b:str) -> str:
    count_a = countDistinctSubsequences(a)
    count_b = countDistinctSubsequences(b)

    if count_a >= count_b:
        return a
    else:
        return b
