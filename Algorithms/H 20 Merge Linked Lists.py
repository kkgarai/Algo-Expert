"""
Merge Linked Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


# O(N+M) time / O(1) space
def mergeTwoLists(headOne, headTwo):
    p1 = headOne
    p1Prev = None
    p2 = headTwo

    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else:
            if p1Prev is not None:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1
    if p1 is None:
        p1Prev.next = p2

    return headOne if headOne.value < headTwo.value else headTwo


# Recursive fn
# O(N+M) time / O(N+M) space
def mergeTwoLists( headOne, headTwo):
    recursiveMerge(headOne, headTwo, None)
    return headOne if headOne.value < headTwo.value else headTwo


def recursiveMerge(self, p1, p2, p1Prev):
    if p1 is None:
        p1Prev.next = p2
        return
    if p2 is None:
        return

    if p1.value < p2.value:
        recursiveMerge(p1.next, p2, p1)
    else:
        if p1Prev is not None:
            p1.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerge(p1, p2.next, p2)
