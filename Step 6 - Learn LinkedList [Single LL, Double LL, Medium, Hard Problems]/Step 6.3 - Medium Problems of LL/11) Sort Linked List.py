#https://www.codingninjas.com/studio/problems/sort-linked-list_625193?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
'''
    Time Complexity: O(N log N) 
    Space Complexity: O(N)

    Where N is number of nodes in the linked list.
'''

def sortList(head):
    
    # Check if the list is empty or contains only one node.
    if head == None or head.next == None:
        return head

    # Initialize a pointer to traverse the linked list
    h = head

    # To store the values of the linked list nodes.
    v = []

    # Step 1: Extract values from the linked list.
    while h != None:
        val = h.data
        v.append(val)
        h = h.next

    # Step 2: Sort the vector in ascending order.
    v.sort()

    # Reset the pointer to the head of the linked list.
    h = head

    # Initialize an index variable to access values from the sorted list.
    i = 0

    # Step 3: Update linked list nodes with sorted values.
    while h != None:
        h.data = v[i]
        h = h.next
        i += 1

    # Return the head of the sorted linked list.
    return head