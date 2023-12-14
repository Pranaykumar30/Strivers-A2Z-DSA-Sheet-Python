#https://www.codingninjas.com/studio/problems/add-two-numbers_1170520?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    dummy = Node()  # Dummy node to initialize the result linked list
    current = dummy
    carry = 0

    while head1 or head2 or carry:
        sum_val = carry

        if head1:
            sum_val += head1.data
            head1 = head1.next
        if head2:
            sum_val += head2.data
            head2 = head2.next

        carry = sum_val // 10
        current.next = Node(sum_val % 10)
        current = current.next

    return dummy.next