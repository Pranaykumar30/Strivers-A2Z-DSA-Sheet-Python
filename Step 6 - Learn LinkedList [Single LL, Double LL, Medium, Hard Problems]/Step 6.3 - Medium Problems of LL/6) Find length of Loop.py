#https://www.codingninjas.com/studio/problems/find-length-of-loop_8160455?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    if not head or not head.next:
        return 0
    
    slow = head.next
    fast = head.next.next
    length = 0
    cycle_exists = False

    while fast and fast.next:
        if slow == fast:
            cycle_exists = True
            break
        slow = slow.next
        fast = fast.next.next
    
    if not cycle_exists:
        return 0

    slow = slow.next
    length += 1
    while slow != fast:
        slow = slow.next
        length += 1
    
    return length