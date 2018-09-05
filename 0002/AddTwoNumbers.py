# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = l3_ = ListNode(0)
        sum = 0
        while True:
            if l1 == None and l2 == None: break
            if l1 != None:
                sum+=l1.val
                l1=l1.next
            if l2 !=None:
                sum+=l2.val
                l2=l2.next
            l3.next = ListNode(sum % 10)
            l3 = l3.next
            sum = sum / 10

        if sum != 0:
            l3.next = ListNode(sum)

        return l3_.next


test = Solution()
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)



l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)




l3 = test.addTwoNumbers(l1,l2)
print l3.val


