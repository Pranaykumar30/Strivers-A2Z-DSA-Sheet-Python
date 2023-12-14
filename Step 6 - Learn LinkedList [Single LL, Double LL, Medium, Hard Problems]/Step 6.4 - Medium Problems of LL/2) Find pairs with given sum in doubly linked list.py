#https://www.codingninjas.com/studio/problems/find-pairs-with-given-sum-in-doubly-linked-list_1164172?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> [[int]]:
    pairs = []
    left = head
    right = head

    # Move 'right' pointer to the end of the list
    while right.next:
        right = right.next

    # Find pairs with sum equal to 'k'
    while left != right and left.data < right.data:
        current_sum = left.data + right.data
        if current_sum == k:
            pairs.append([left.data, right.data])
            left = left.next
            right = right.prev
        elif current_sum < k:
            left = left.next
        else:
            right = right.prev

    return pairs
