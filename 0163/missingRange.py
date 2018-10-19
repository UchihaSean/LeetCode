class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        ans = []
        if lower < nums[0]:
            if lower == nums[0] - 1:
                ans.append(str(lower))
            else:
                ans.append(str(lower) + "->" + str(nums[0] - 1))
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i] - 1:
                if nums[i - 1] == nums[i] - 2:
                    ans.append(str(nums[i - 1] + 1))
                else:
                    ans.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
        if upper > nums[-1]:
            if upper == nums[-1] + 1:
                ans.append(str(upper))
            else:
                ans.append(str(nums[-1] + 1) + "->" + str(upper))
        return ans
