#https://www.codingninjas.com/studio/problems/word-break-1_758963?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def getAllValidSentences(s: str, dictionary: List[str]) -> List[str]:
    def backtrack(start, path):
        if start == len(s):
            result.append(' '.join(path))
            return

        for word in dictionary:
            if s.startswith(word, start):
                path.append(word)
                backtrack(start + len(word), path)
                path.pop()

    result = []
    backtrack(0, [])
    return result
