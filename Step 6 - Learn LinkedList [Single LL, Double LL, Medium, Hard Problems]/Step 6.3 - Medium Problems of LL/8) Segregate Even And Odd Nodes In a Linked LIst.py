'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def segregateEvenOdd(head):
    if head is None or head.next is None:
        return head

    even_head, odd_head = None, None
    even_tail, odd_tail = None, None
    current = head

    while current:
        if current.data % 2 == 0:  # Even node
            if even_head is None:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = even_tail.next
        else:  # Odd node
            if odd_head is None:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
        current = current.next

    if even_tail:
        even_tail.next = odd_head
    else:
        return odd_head

    if odd_tail:
        odd_tail.next = None

    return even_head