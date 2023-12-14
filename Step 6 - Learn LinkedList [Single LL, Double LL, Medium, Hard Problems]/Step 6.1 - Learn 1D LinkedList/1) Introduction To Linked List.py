#https://www.codingninjas.com/studio/problems/introduction-to-linked-list_8144737?utm_source=youtube&utm_medium=affiliate&utm_campaign=Codestudio_Linkedlistseries
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    if not arr:
        return None

    # Create the head node
    head = Node(arr[0])
    current = head

    # Iterate through the array to create the linked list
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node

    return head