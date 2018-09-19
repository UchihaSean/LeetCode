class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [nums[0]]
        right = [nums[-1]]
        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i])
            right.append(right[-1] * nums[-i - 1])

        ans = []
        # print(left)
        # print(right)
        for i in range(len(nums)):
            now = 0
            if i == 0:
                now = right[len(nums) - 2]
            elif i == len(nums) - 1:
                now = left[len(nums) - 2]
            else:
                now = left[i - 1] * right[len(nums) - i - 2]
            ans.append(now)
        return ans
