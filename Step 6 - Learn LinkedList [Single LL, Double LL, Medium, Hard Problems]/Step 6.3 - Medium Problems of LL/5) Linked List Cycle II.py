'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''
#https://www.codingninjas.com/studio/problems/linked-list-cycle-ii_1112628?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def firstNode(head):
    slow = head
    fast = head
    
    # Detect if there's a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    # No cycle present
    if fast is None or fast.next is None:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow