class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]

        fmax = [0]
        fmin = [0]

        for num in nums:
            fmax.append(max(fmax[-1]*num, fmin[-1]*num, num))
            fmin.append(min(fmax[-2]*num, fmin[-1]*num, num))

        return max(fmax)


test = Solution()
print test.maxProduct([-4, -3, -2])
