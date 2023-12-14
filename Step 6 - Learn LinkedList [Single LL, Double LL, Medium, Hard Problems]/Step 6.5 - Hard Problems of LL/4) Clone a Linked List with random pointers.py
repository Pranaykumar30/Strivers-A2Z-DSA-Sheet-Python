#https://www.codingninjas.com/studio/problems/clone-a-linked-list-with-random-pointers_983604?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, data=0, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random


# Don't change the code above.


def cloneLL(head: Node) -> Node:
    # Write your code here
    if not head:
        return None

    # Create a mapping to store the original node and its corresponding copy
    mapping = {}

    # Create copies of each node without setting their 'random' pointers initially
    current = head
    while current:
        mapping[current] = Node(current.data)
        current = current.next

    # Assign 'next' and 'random' pointers for each copied node
    current = head
    while current:
        mapping[current].next = mapping.get(current.next)
        mapping[current].random = mapping.get(current.random)
        current = current.next

    return mapping[head]