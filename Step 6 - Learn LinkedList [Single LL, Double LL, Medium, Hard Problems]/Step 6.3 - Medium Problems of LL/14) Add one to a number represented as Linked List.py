#https://www.codingninjas.com/studio/problems/add-one-to-a-number-represented-as-linked-list_920557?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.
def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def addOne(head: Node) -> Node:
    head = reverseLinkedList(head)
    current = head
    carry = 1

    while current and carry:
        total = current.data + carry
        current.data = total % 10
        carry = total // 10

        if carry and not current.next:
            current.next = Node(carry)
            break

        current = current.next

    return reverseLinkedList(head)