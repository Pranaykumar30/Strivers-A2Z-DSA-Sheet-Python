#https://www.codingninjas.com/studio/problems/sort-linked-list-of-0s-1s-2s_1071937?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def sortList(head):
    if not head or not head.next:
        return head
    
    count = [0, 0, 0]  # Count occurrences of 0, 1, 2
    current = head

    # Count occurrences of each value
    while current:
        count[current.data] += 1
        current = current.next
    
    current = head
    i = 0

    # Modify the linked list values based on count
    while current:
        if count[i] == 0:
            i += 1
        else:
            current.data = i
            count[i] -= 1
            current = current.next

    return head