# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def sort(self, head):
        if head.next == None: return head

        slow = fast = head
        while True:
            if fast == None or fast.next == None or fast.next.next == None: break
            fast = fast.next.next
            slow = slow.next

        right = self.sort(slow.next)
        slow.next = None
        left = self.sort(head)

        node = pre = ListNode(-1)
        while left and right:
            if left.val<right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        if left: node.next = left
        if right: node.next = right

        return pre.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        return self.sort(head)
