#https://www.codingninjas.com/studio/problems/maximum-nesting-depth-of-the-parentheses_8144741?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def maxDepth(s:str) -> int:
    max_depth = 0
    curr_depth = 0
    
    for char in s:
        if char == '(':
            curr_depth += 1
            max_depth = max(max_depth, curr_depth)
        elif char == ')':
            curr_depth -= 1
    
    return max_depth