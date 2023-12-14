#https://www.codingninjas.com/studio/problems/reverse-list-in-k-groups_983644?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from os import *
from sys import *
from collections import *
from math import *

'''
    # Linked List Node structure for reference

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''
def getLength(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def kReverse(head, k):
    if not head:
        return head

    length = getLength(head)

    if length < k:
        return head

    prev = None
    curr = head
    forward = head.next
    count = 0

    while count < k:
        curr.next = prev
        prev = curr
        curr = forward
        if forward:
            forward = forward.next
        count += 1

    head.next = kReverse(curr, k)

    return prev