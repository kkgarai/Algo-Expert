"""
Find Loops
Given a linked list we need to find the node at which the loop originates.
"""


# O(N) time / O(1) space
def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next

    first = head
    while first != second:
        first = first.next
        second = second.next

    return first
