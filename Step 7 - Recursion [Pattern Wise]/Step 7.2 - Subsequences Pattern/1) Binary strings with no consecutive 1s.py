#https://www.codingninjas.com/studio/problems/-binary-strings-with-no-consecutive-1s._893001?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def generateString(N: int) -> List[str]:
    def generateHelper(curr_string, index):
        if index == N:
            result.append(curr_string)
            return
        if len(curr_string) == 0 or curr_string[-1] == '0':
            generateHelper(curr_string + '0', index + 1)
            generateHelper(curr_string + '1', index + 1)
        elif curr_string[-1] == '1':
            generateHelper(curr_string + '0', index + 1)

    result = []
    generateHelper('', 0)
    return result