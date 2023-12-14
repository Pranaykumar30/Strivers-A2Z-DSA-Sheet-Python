'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''
#https://www.codingninjas.com/studio/problems/count-nodes-of-linked-list_5884?utm_source=youtube&utm_medium=affiliate&utm_campaign=Codestudio_Linkedlistseries
def length(head) :
    #Your code goes here
    if not head:
        return 0
    
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    return count