'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''



def isPalindrome(head):
    def reverse_linked_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    reversed_head = reverse_linked_list(head)
    iter1, iter2 = head, reversed_head

    while iter1 and iter2:
        if iter1.data != iter2.data:
            return False
        iter1 = iter1.next
        iter2 = iter2.next

    return True