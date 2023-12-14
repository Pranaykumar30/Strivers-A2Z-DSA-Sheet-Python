'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def deleteMiddle(head):
    if head.next is None:
        return None

    prev = slow = fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head