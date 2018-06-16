# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        merge_sorted = l3 = ListNode(0)
        while True:
            if l1 == None or l2 == None: break
            if l1.val>l2.val:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
            else:
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next

        while l1 != None:
            l3.next = ListNode(l1.val)
            l1 = l1.next
            l3 = l3.next
        while l2 != None:
            l3.next = ListNode(l2.val)
            l2 = l2.next
            l3 = l3.next
        return merge_sorted.next





l1 = ListNode(1,5)
l2 = ListNode(6)
test = Solution()
print test.mergeTwoLists(l1,l2)