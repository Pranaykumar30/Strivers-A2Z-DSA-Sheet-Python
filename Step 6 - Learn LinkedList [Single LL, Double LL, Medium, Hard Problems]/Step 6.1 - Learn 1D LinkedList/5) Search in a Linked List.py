'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''
#https://www.codingninjas.com/studio/problems/search-in-a-linked-list_975381?utm_source=youtube&utm_medium=affiliate&utm_campaign=Codestudio_Linkedlistseries
def searchInLinkedList(head, k):
    # Your code goes here.
    current = head
    while current:
        if current.data == k:
            return 1
        current = current.next
    return 0