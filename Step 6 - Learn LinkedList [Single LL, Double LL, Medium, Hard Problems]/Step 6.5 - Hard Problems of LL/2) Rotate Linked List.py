#https://www.codingninjas.com/studio/problems/rotate-linked-list_920454?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def rotate(head: Node, k: int) -> Node:
    # Write your code here.
    if not head or k == 0:
        return head

    # Calculate the length of the linked list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next

    # Calculate the actual rotation
    k = k % length
    if k == 0:
        return head

    # Find the new head after rotation
    new_head_position = length - k - 1
    current.next = head  # Make the list circular
    current = head

    # Traverse to the new head position
    while new_head_position > 0:
        current = current.next
        new_head_position -= 1

    new_head = current.next
    current.next = None

    return new_head