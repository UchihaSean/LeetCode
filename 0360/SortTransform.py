class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        ans = []
        if a == 0:
            for num in nums:
                ans.append(num * b + c)
            if b < 0: ans = ans[::-1]
            return ans
        else:
            mid = -(b + 0.0) / 2 / a
            index = 0
            min_dis = 9999999999
            for i in range(len(nums)):
                if abs(nums[i] - mid) < min_dis:
                    min_dis = abs(nums[i] - mid)
                    index = i
            ans.append(a * nums[index] ** 2 + b * nums[index] + c)
            l = index - 1
            r = index + 1
            while l >= 0 and r < len(nums):
                if nums[r] - mid > mid - nums[l]:
                    ans.append(a * nums[l] ** 2 + b * nums[l] + c)
                    l -= 1
                else:
                    ans.append(a * nums[r] ** 2 + b * nums[r] + c)
                    r += 1
            while l >= 0:
                ans.append(a * nums[l] ** 2 + b * nums[l] + c)
                l -= 1
            while r < len(nums):
                ans.append(a * nums[r] ** 2 + b * nums[r] + c)
                r += 1
            if a > 0:
                return [int(s) for s in ans]

            return [int(s) for s in ans][::-1]




