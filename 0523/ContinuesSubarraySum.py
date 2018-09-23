class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True
        if k == 0: return False
        mod_k = set([0])
        now = [nums[0]]
        for i in range(1, len(nums)):
            now.append(now[-1] + nums[i])
            if now[-1] % k in mod_k:
                return True
            if i > 0:
                mod_k.add(now[i - 1] % k)
        return False