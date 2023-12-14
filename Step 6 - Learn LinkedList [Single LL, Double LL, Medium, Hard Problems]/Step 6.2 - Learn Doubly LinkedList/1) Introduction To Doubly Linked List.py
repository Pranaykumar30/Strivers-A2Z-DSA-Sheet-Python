#https://www.codingninjas.com/studio/problems/introduction-to-doubly-linked-list_8160413?utm_source=youtube&utm_medium=affiliate&utm_campaign=Codestudio_Linkedlistseries
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def constructDLL(arr: [int]) -> Node:
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        current.next = new_node
        new_node.prev = current
        current = new_node
    
    return head