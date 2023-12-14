#https://www.codingninjas.com/studio/problems/delete-node-of-linked-list_8160463?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(list: Node) -> Node:
    if not list or not list.next:
        return None
    
    current = list
    while current.next.next:
        current = current.next
    
    current.next = None
    return list