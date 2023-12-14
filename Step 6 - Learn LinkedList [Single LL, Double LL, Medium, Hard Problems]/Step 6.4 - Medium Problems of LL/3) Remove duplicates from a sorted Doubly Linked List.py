#https://www.codingninjas.com/studio/problems/remove-duplicates-from-a-sorted-doubly-linked-list_2420283?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    # Write your code here
    current = head

    while current and current.next:
        if current.data == current.next.data:
            next_next = current.next.next
            current.next = next_next
            if next_next:
                next_next.prev = current
        else:
            current = current.next

    return head
