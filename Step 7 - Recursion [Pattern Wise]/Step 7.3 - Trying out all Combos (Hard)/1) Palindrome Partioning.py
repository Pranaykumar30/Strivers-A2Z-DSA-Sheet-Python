#https://www.codingninjas.com/studio/problems/palindrome-partitioning_626181?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def partition(string: str) -> List[List[str]]:
    def is_palindrome(s):
        return s == s[::-1]

    def backtrack(start, path):
        if start == len(string):
            result.append(path[:])
            return

        for end in range(start + 1, len(string) + 1):
            substring = string[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result
