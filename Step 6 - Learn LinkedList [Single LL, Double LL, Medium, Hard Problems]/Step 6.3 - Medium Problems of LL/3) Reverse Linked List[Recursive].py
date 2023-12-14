def reverseLinkedList(head):
    if not head or not head.next:
        return head
    
    new_head = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    
    return new_head