#https://www.codingninjas.com/studio/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    dummy = Node(0)  # Create a dummy node to handle the case where the first node needs to be removed
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.data == k:
            current.next = current.next.next
            if current.next:
                current.next.prev = current
        else:
            current = current.next

    return dummy.next