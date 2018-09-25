class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        ans = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= s:
                if ans == 0 or ans > right - left + 1:
                    ans = right - left + 1
                total -= nums[left]
                left += 1
        return ans
