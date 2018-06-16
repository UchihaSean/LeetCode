class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        length=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                length+=1
        return length


test = Solution()
print test.removeDuplicates([1,1,1,1,1,2,2,5,5,5,5])