"""
Reverse Linked List
"""


# O(N) time / O(1) space
def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
