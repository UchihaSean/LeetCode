class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict = {0: -1}
        max_length = 0
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in dict and i - dict[pre - k] > max_length:
                max_length = i - dict[pre - k]
            if pre not in dict:
                dict[pre] = i
        return max_length


