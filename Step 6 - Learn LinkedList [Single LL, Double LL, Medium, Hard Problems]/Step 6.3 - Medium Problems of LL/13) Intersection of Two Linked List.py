#https://www.codingninjas.com/studio/problems/-intersection-of-two-linked-lists_630457?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def findIntersection(firstHead, secondHead):
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def moveAhead(head, steps):
        while steps > 0:
            head = head.next
            steps -= 1
        return head

    firstLength = getLength(firstHead)
    secondLength = getLength(secondHead)

    diff = abs(firstLength - secondLength)

    if firstLength > secondLength:
        firstHead = moveAhead(firstHead, diff)
    else:
        secondHead = moveAhead(secondHead, diff)

    while firstHead and secondHead:
        if firstHead == secondHead:
            return firstHead
        firstHead = firstHead.next
        secondHead = secondHead.next

    return None