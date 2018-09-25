class Solution(object):
    def binary_search(self, pre, num):
        l = -1
        r= len(pre)-1
        while l+1<r:
            mid = (l+r)/2
            if pre[mid]>=num:
                r = mid
            else:
                l = mid
        return r
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = []
        for num in nums:
            # print(pre)
            if len(pre) == 0 or num>pre[-1]:
                pre.append(num)
            else:
                index = self.binary_search(pre, num)

                pre[index] = num
        return len(pre)

test = Solution()
print test.lengthOfLIS([4,10,4,3,8,9])
# print test.binary_search([1,2,5,8,10], 3)