# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        orign_small = small = ListNode(0)
        orign_large = large = ListNode(0)

        while head:
            if head.val<x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None
        small.next = orign_large.next

        return orign_small.next


head = ListNode(2)
head.next = ListNode(1)

test = Solution()
test.partition(head,2)