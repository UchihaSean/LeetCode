# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        tmp = ListNode(-1)
        tmp.next = head
        pre = tmp
        tmp = tmp.next
        while True:
            after = tmp
            tmp = tmp.next
            after.next = pre
            pre = after
