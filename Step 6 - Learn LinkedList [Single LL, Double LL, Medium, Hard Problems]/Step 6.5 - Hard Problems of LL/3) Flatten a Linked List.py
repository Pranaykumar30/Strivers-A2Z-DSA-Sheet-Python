#https://www.codingninjas.com/studio/problems/flatten-a-linked-list_1112655?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

def flattenLinkedList(head: Node) -> Node:
    if not head or not head.next:
        return head

    new_list = flattenLinkedList(head.next)
    head.next = None

    result = Node(0)
    result_itr = result

    while head and new_list:
        if head.data < new_list.data:
            result_itr.child = head
            result_itr = result_itr.child
            head = head.child
        else:
            result_itr.child = new_list
            result_itr = result_itr.child
            new_list = new_list.child

    if head:
        result_itr.child = head
    else:
        result_itr.child = new_list

    return result.child