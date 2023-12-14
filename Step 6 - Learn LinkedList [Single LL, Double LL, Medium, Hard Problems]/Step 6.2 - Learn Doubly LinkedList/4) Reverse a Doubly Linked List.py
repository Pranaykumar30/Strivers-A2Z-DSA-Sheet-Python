'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''
#https://www.codingninjas.com/studio/problems/reverse-a-doubly-linked-list_1116098?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def reverseDLL(head):
    # Write your code here
    if not head or not head.next:
        return head
    
    current = head
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    
    return temp.prev