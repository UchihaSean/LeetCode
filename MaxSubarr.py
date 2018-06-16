class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mininum = 0
        max_sub_sum = nums[0]
        for i in range(len(nums)):
            if i>0: nums[i] += nums[i-1]
            if max_sub_sum< nums[i] - mininum:
                max_sub_sum = nums[i] - mininum
            if mininum > nums[i]: mininum = nums[i]



        return max_sub_sum





test = Solution()
print test.maxSubArray([1,2])