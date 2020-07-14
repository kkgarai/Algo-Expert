"""
Add two numbers as a linked list
eg:
342+465=807
2 -> 4 -> 3 + 5 -> 6 -> 4 = 7 -> 0 -> 8
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Iterative
        return self.addTwoNumbersIterative(l1, l2)
        # Recursive
        # return self.addTwoNumbersHelper(l1,l2,0)

    def addTwoNumbersIterative(self, l1, l2):
        a = l1
        b = l2
        c = 0
        ret = current = None

        while a or b:
            val = a.val + b.val + c
            c = val // 10
            if not current:
                ret = current = Node(val % 10)
            else:
                current.next = Node(val % 10)
                current = current.next
            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            a = a.next
            b = b.next
        return ret

    def addTwoNumbersHelper(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next = self.addTwoNumbersHelper(l1.next, l2.next, c)
        return ret


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print(answer.val)
    answer = answer.next
