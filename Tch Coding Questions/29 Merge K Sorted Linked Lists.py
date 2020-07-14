"""
Merge K Sorted Linked Lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = current = ListNode(-1)
        while any(list is not None for list in lists):
            current_min,i=min((list.val,i) for i,list in enumerate(lists) if list is not None)
            lists[i]=lists[i].next
            current.next=ListNode(current_min)
            current=current.next
        return head.next

