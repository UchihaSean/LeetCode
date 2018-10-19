class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l+1<r:
            mid = (l+r)/2
            count = 0
            for num in nums:
                if num<=mid:
                    count+=1
            if count> mid:
                r = mid
            else:
                l = mid
        return r