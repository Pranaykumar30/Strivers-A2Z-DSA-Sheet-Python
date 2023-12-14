
#Following is the structure of the Node class already defined.
#https://www.codingninjas.com/studio/problems/cycle-detection-in-a-singly-linked-list_628974?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def detectCycle(head) :
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    
    return False