class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        now = 0
        dict = {0: 1}
        ans = 0
        for i in range(len(nums)):
            now += nums[i]
            if now - k in dict:
                ans += dict[now - k]
            if now in dict:
                dict[now] += 1
            else:
                dict[now] = 1

        return ans