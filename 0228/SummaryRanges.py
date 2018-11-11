class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        ans = []
        now = nums[0]
        nums.append(-99999999)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                if nums[i - 1] == now:
                    ans.append(str(now))
                else:
                    ans.append(str(now) + "->" + str(nums[i - 1]))
                now = nums[i]
        return ans
