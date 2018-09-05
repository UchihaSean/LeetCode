# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        tmp = cur = ListNode(-1)
        tmp.next = head
        cur.next = head


        while True:
            tmp = cur
            head_pre = head
            head = head.next
            if head == None: break
            while True:
                pre = tmp
                tmp = tmp.next
                if tmp.val >= head.val: break
            if tmp==head: continue
            head_after = head.next
            pre.next = head
            head.next = tmp
            head = head_pre
            head_pre.next = head_after

        return cur.next


head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(1)

test = Solution()
tail = test.insertionSortList(head)
print tail.val, tail.next.val, tail.next.next.val
