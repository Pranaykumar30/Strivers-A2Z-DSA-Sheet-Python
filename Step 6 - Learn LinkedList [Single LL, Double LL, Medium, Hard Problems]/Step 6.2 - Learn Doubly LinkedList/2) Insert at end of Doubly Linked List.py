#https://www.codingninjas.com/studio/problems/insert-at-end-of-doubly-linked-list_8160464?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.


def insertAtTail(head: Node, k: int) -> Node:
    new_node = Node(k)
    
    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    new_node.prev = current
    
    return head