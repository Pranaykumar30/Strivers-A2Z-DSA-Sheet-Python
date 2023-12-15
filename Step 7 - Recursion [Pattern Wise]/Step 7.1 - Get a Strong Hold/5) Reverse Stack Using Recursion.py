#https://www.codingninjas.com/studio/problems/reverse-stack-using-recursion_631875?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List
def insertAtBottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.append(temp)
def reverseStack(stack: List[int]) -> None:
    if len(stack) > 0:
        temp = stack.pop()
        reverseStack(stack)
        insertAtBottom(stack, temp)