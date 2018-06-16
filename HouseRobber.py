class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        f = [0 for _ in range(len(nums))]
        maxF = 0

        for i in range(len(nums)):
            if i > 1:
                maxF = max(maxF, f[i - 2])
            f[i] = maxF + nums[i]

        return max(f)


test = Solution()
print test.rob([2, 7, 9, 3, 1])
