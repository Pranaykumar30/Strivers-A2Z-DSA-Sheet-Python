'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    if head is None:
        return None

    class Node:  # Redefine the Node class within the function
        def __init__(self, data):
            self.data = data
            self.next = None

    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast pointer to the Kth node from the start
    for _ in range(k):
        if fast is None:
            return None  # K is greater than the length of the linked list
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove the Kth node
    slow.next = slow.next.next

    return dummy.next 