class Solution(object):
    def find(self, nums, l, r, k):
        # print(l, r, k)
        if l == r: return nums[l]
        pivot = nums[r]
        index = l - 1
        for i in range(l, r + 1):
            if nums[i] < pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        if index - l + 1 == k: return pivot
        if index - l >= k:
            return self.find(nums, l, index, k)
        else:
            return self.find(nums, index + 1, r - 1, k - (index - l) - 2)

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        kth1 = self.find(nums, 0, len(nums) - 1, (len(nums) - 1) / 2)
        kth2 = self.find(nums, 0, len(nums) - 1, len(nums) / 2)
        kth = (kth1 + kth2 + 0.0) / 2
        # print(kth1, kth2)
        l = 1
        r = 2 * ((len(nums) - 1) / 2)
        while l < len(nums) and nums[l] > kth: l += 2
        while r > -1 and nums[r] < kth: r -= 2
        for i in range(len(nums)):
            if nums[i] > kth:
                if i <= l and i % 2 == 1: continue
                while l < len(nums) and nums[l] > kth: l += 2
                if l >= len(nums): break
                nums[i], nums[l] = nums[l], nums[i]
                l += 2
        # print(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < kth:
                if i >= r and i % 2 == 0: continue
                while r > -1 and nums[r] < kth: r -= 2
                if r < 0: break
                nums[i], nums[r] = nums[r], nums[i]
                r -= 2









