#https://www.codingninjas.com/studio/problems/middle-of-linked-list_973250?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from math import *
from collections import *
from sys import *
from os import *



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def findMiddle(head):
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow